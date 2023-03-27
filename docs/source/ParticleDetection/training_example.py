import os

import numpy as np
from detectron2.config import CfgNode
import detectron2.data.transforms as T

from ParticleDetection.modelling.runners import training
import ParticleDetection.utils.datasets as ds
import ParticleDetection.modelling.datasets as mod_ds
import ParticleDetection.modelling.configs as mod_config
import ParticleDetection.modelling.augmentations as ca


def init_cfg() -> dict:
    """Initialize the configuration for training.
    Returns
    -------
    dict
        Configuration that can be used for training as:
            `training.run_training(**configuration)`
    """
    # Set up known dataset(s) for use with Detectron2 #########################
    data_folder = "./test_dataset"
    metadata_file = "/metadata.json"
    train_data = ds.DataSet("dataset_training", data_folder + "/training",
                            metadata_file)
    val_data = ds.DataSet("dataset_validation", data_folder + "/validation",
                          metadata_file)
    # Register datasets to Detectron2
    classes = ["blue", "green", "orange", "purple", "red", "yellow",
               "black", "lilac", "brown"]
    try:
        mod_ds.register_dataset(train_data, classes=classes)
        mod_ds.register_dataset(val_data, classes=classes)
    except AssertionError as e:
        # Datasets are already registered
        print(e)
    image_no = mod_ds.get_dataset_size(train_data)

    # Set up training configuration ###########################################
    # Load a *.yaml file with static configurations
    cfg = CfgNode(CfgNode.load_yaml_with_base(
        "your_starting_configuration.yaml"))

    cfg.DATASETS.TRAIN = [train_data.name]
    cfg.DATASETS.TEST = [val_data.name]

    # control the GPU memory load
    cfg.SOLVER.IMS_PER_BATCH = 1
    # No warm-up and constant lr
    cfg.SOLVER.WARMUP_ITERS = 0
    cfg.SOLVER.STEPS = ()
    cfg.SOLVER.CHECKPOINT_PERIOD = 5 * image_no

    # add computed values to the configuration,
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(
        ds.get_dataset_classes(train_data))
    cfg.MODEL.BACKBONE.FREEZE_AT = 0
    cfg.TEST.EVAL_PERIOD = int(image_no / cfg.SOLVER.IMS_PER_BATCH)
    counts = ds.get_object_counts(val_data)
    cfg.TEST.DETECTIONS_PER_IMAGE = int(1.5 * np.max(counts))

    # create a list of image augmentations to use #############################
    augmentations = [
        ca.SomeOf([
            T.RandomFlip(horizontal=True, vertical=False),
            T.RandomFlip(horizontal=False, vertical=True),
            T.RandomRotation([90, 180, 270], expand=False,
                             sample_style="choice"),
            T.RandomRotation([15, 30, 45, 60, 75], expand=False,
                             sample_style="choice"),
            ca.MultiplyAugmentation(mul=(0.85, 1.15)),
            ca.GaussianBlurAugmentation(sigmas=(0.0, 2.0)),
            ca.SharpenAugmentation(alpha=(0.0, 0.5), lightness=(0.8, 1.15))
        ],
            lower=0, upper=3)
    ]

    return {
        "train_set": train_data,
        "val_set": val_data,
        "configuration": cfg,
        "output_dir": "",
        "resume": True,
        "visualize": False,
        "img_augmentations": augmentations,
        "freeze_layers": []
    }


def train_heads(output_base: str, config: dict, weights: str = None) -> dict:
    """Training Step 1
    Trains only the heads of the model, i.e. excludes backbone and box
    predictor from updating during training.
    Parameters
    ----------
    output_base : str
        Path to the main output directory. Will serve as the location for the
        output folder generated by this training step.
    config : dict
        Basic configuration of the model training. Will be adapted in this
        function.
    weights : str, optional
        Path to a *.pkl file containing weights to be used for the trained
        model.
    Returns
    -------
    dict
        Configuration used for training the model in this training step.
    """
    config["freeze_layers"] = ["backbone", "box_predictor"]
    previous_output = config["output_dir"]
    config["output_dir"] = os.path.join(output_base, "heads")
    if weights is None:
        config["configuration"].MODEL.WEIGHTS = os.path.join(
            previous_output, "model_final.pth")
    else:
        config["configuration"].MODEL.WEIGHTS = weights

    image_no = mod_ds.get_dataset_size(config["train_set"])
    config["configuration"].SOLVER.MAX_ITER = int(
        mod_config.get_iters(config["configuration"], image_no,
                             desired_epochs=300))
    config["configuration"].SOLVER.BASE_LR = 0.001
    config["configuration"].INPUT.CROP.ENABLED = True
    config["configuration"].INPUT.MIN_SIZE_TRAIN = 512

    training.run_training(**config)
    return config


def train_all_s1(output_base: str, config: dict, weights: str = None) -> dict:
    """Training Step 2
    Trains all layers of the model with the same learning rate as in step 1.
    Parameters
    ----------
    output_base : str
        Path to the main output directory. Will serve as the location for the
        output folder generated by this training step.
    config : dict
        Basic configuration of the model training. Will be adapted in this
        function.
    weights : str, optional
        Path to a *.pkl file containing weights to be used for the trained
        model.
    Returns
    -------
    dict
        Configuration used for training the model in this training step.
    """
    config["freeze_layers"] = []
    previous_output = config["output_dir"]
    config["output_dir"] = os.path.join(output_base, "all_1")
    if weights is None:
        config["configuration"].MODEL.WEIGHTS = os.path.join(
            previous_output, "model_final.pth")
    else:
        config["configuration"].MODEL.WEIGHTS = weights
    image_no = mod_ds.get_dataset_size(config["train_set"])
    config["configuration"].SOLVER.MAX_ITER = int(
        mod_config.get_iters(config["configuration"], image_no,
                             desired_epochs=450))

    training.run_training(**config)
    return config


if __name__ == "__main__":
    output = "./example_detector"
    init_weights = "https://dl.fbaipublicfiles.com/detectron2/COCO-InstanceSegmentation/mask_rcnn_R_101_FPN_3x/138205316/model_final_a3ec72.pkl"
    cfg = init_cfg()
    cfg = train_heads(output, cfg, init_weights)
    cfg = train_all_s1(output, cfg)
