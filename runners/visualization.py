import os
import sys
import cv2
import random
import logging
from typing import Union, Iterable

import matplotlib.pyplot as plt
import matplotlib as mpl
import torch
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer, GenericMask

import utils.datasets as ds

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.INFO)
formatter = logging.Formatter(
    "[%(asctime)s] %(name)s %(levelname)s: %(message)s",
    datefmt="%m/%d %H:%M:%S"
    )
ch.setFormatter(formatter)
_logger.addHandler(ch)


def visualize(prediction, original: Union[dict, str],
              hide_tags=True, output_dir="", colors: Iterable = None):
    """Visualizes predictions on one image with it's ground truth."""
    if isinstance(original, dict):
        im = cv2.imread(original["file_name"])
    else:
        im = cv2.imread(original)

    # Remove unnecessary information before drawing
    to_draw = prediction["instances"].to("cpu")
    if hide_tags:
        del to_draw._fields["scores"]
        del to_draw._fields["pred_boxes"]

    fig = None
    if isinstance(original, dict):
        # Display original as well
        fig_title = os.path.basename(original["file_name"])
        fig = create_figure(im, to_draw, original, colors)
    else:
        fig_title = os.path.basename(original)
        fig = create_figure(im, to_draw, None, colors)

    if not hide_tags:
        if "pred_keypoints" in to_draw._fields:
            # Keypoint visualization
            ax = fig.axes[0]
            kps = to_draw.pred_keypoints.numpy()
            ax.plot(kps[:, 0, 0:2].squeeze().T, kps[:, 1, 0:2].squeeze().T)

    if output_dir:
        plt.savefig(os.path.join(output_dir, fig_title))


def create_figure(img, predictions, gt: dict = None, colors: Iterable = None):
    width, height = img.shape[1], img.shape[0]
    if colors is None:
        colors = plt.get_cmap("tab10").colors

    def add_outlines(mask_data, axes, color=None, confidences=None):
        if isinstance(mask_data, torch.Tensor):
            mask_data = mask_data.numpy()
        masks = [GenericMask(x, height, width) for x in mask_data]
        for m, c, s in zip(masks, color, confidences):
            for segment in m.polygons:
                polygon = mpl.patches.Polygon(
                    segment.reshape(-1, 2),
                    fill=False,
                    color=c
                )
                axes.add_patch(polygon)
            axes.text(*m.bbox()[0:2], f"{s.numpy():.2f}")
        return axes

    def get_colors(len_data, class_data=None):
        if class_data is None:
            return len_data*["black"]
        else:
            return [colors[lbl] for lbl in class_data]
    try:
        scores = predictions.scores
    except KeyError:
        scores = None

    fig = plt.figure(frameon=False)
    dpi = fig.get_dpi()
    # add a small 1e-2 to avoid precision lost due to matplotlib's truncation
    # (https://github.com/matplotlib/matplotlib/issues/15363)
    if gt:
        fig.set_size_inches(
            (width + 1e-2) / dpi,
            2 * (height + 1e-2) / dpi,
        )
        # Prediction axes
        ax1 = fig.add_axes([0, .5, 1, .5])
        ax1.imshow(img)
        ax1.axis("off")
        try:
            class_colors = get_colors(len(predictions.pred_classes),
                                    predictions.pred_classes)
            add_outlines(predictions.pred_masks, ax1, class_colors, scores)
        except AttributeError:
            # predictions does not have mask data, e.g. because it predicted 
            # only keypoints
            _logger.info("Predictions don't have segmentation masks. "
                         "Skipping mask visualization...")

        # Groundtruth axes
        ax2 = fig.add_axes([0, 0, 1, .5])
        ax2.imshow(img)
        ax2.axis("off")
        try:
            gt_masks = [anno["segmentation"] for anno in gt["annotations"]]
            gt_classes = [anno["category_id"] for anno in gt["annotations"]]
            class_colors = get_colors(len(gt_classes), gt_classes)
            add_outlines(gt_masks, ax2, class_colors)
        except IndexError:
            # annotations don't have the "segmentation" field, e.g. because 
            # they only have keypoints
            _logger.info("Ground-truth does not have segmentation masks. "
                         "Skipping mask visualization...")

    else:
        fig.set_size_inches(
            (width + 1e-2) / dpi,
            (height + 1e-2) / dpi,
        )
        # Prediction axes
        ax1 = fig.add_axes([0, 0, 1, 1])
        ax1.imshow(img)
        ax1.axis("off")
        try:
            class_colors = get_colors(len(predictions.pred_classes),
                                    predictions.pred_classes)
            add_outlines(predictions.pred_masks, ax1, class_colors, scores)
        except AttributeError:
            # predictions does not have mask data, e.g. because it predicted 
            # only keypoints
            _logger.info("Predictions don't have segmentation masks. "
                         "Skipping mask visualization...")

    return fig


def vis_single(dataset, filenames):
    filename = "FT2015_shot2_gp2_00750.jpg"
    dataset_dicts = ds.load_custom_data(dataset)
    meta_data = MetadataCatalog.get(dataset.name)

    for d in random.sample(dataset_dicts, 5):
        img = cv2.imread(d["file_name"])
        visualizer = Visualizer(img[:, :, ::-1], metadata=meta_data, scale=0.5)
        # d["annotations"] = random.sample(d["annotations"], 10)
        out = visualizer.draw_dataset_dict(d)
        plt.figure(figsize=[12.80, 7.20])
        plt.imshow(out.get_image()[:, :, ::-1])
        plt.show()


if __name__ == "__main__":
    data_folder = "../datasets/rods_c4m"
    metadata_file = "/via_export_json.json"
    val_data = ds.DataSet("c4m_val", data_folder + "/val", metadata_file)
    classes = ["blue", "green", "orange", "purple", "red", "yellow", "black",
               "lilac", "brown"]
    ds.register_dataset(val_data, classes=classes)

    vis_single(val_data, 1)
