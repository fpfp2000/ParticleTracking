#  Copyright (c) 2023 Adrian Niemann Dmitry Puzyrev
#
#  This file is part of ParticleDetection.
#  ParticleDetection is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ParticleDetection is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with RodTracker.  If not, see <http://www.gnu.org/licenses/>.

"""
Functions to prepare datasets for the use by the Detectron2 framework, as well
as functions to get basic information about a dataset, i.e. size and thing
classes.

**Author:**     Adrian Niemann (adrian.niemann@ovgu.de)\n
**Date:**       31.10.2022

"""
import os
import json
import warnings
from typing import List, Callable, Set

import numpy as np
from PIL import Image
from detectron2.structures import BoxMode
from detectron2.data import DatasetCatalog, MetadataCatalog

from ParticleDetection.utils.datasets import DataSet


def load_custom_data(dataset: DataSet) -> List[dict]:
    """Loads a (training/testing) dataset into the Detectron2 format.

    Parameters
    ----------
    dataset : DataSet
        Dataset that will be transferred to the Detectron2 dataset format for
        training a model.

    Returns
    -------
    List[dict]
        Dataset in the Detectron2 format.

    Note
    ----
    For more information see:
    https://detectron2.readthedocs.io/en/latest/tutorials/datasets.html#standard-dataset-dicts
    """
    with open(dataset.annotation) as metadata:
        annotations = json.load(metadata)

    custom_data = []
    for idx, val in enumerate(annotations.values()):
        # Skip non-annotated image entries
        if not val["regions"]:
            continue

        # Create an entry in the custom dataset
        record = {}
        filename = os.path.join(dataset.folder, val["filename"])
        width, height = Image.open(filename).size[:2]
        record["file_name"] = filename
        record["image_id"] = idx
        record["width"] = width
        record["height"] = height

        annos = val["regions"]
        objs = []
        for anno in annos:
            try:
                category_id = int(anno["region_attributes"]["rod_col"])
            except KeyError:
                category_id = 0
            if "keypoints" in anno:
                keypoints = anno["keypoints"]
            else:
                keypoints = None

            anno = anno["shape_attributes"]
            px = anno["all_points_x"]
            py = anno["all_points_y"]
            # TODO: verify the polygon computation in the following two lines
            poly = [(x + 0.5, y + 0.5) for x, y in zip(px, py)]
            poly = [p for x in poly for p in x]

            obj = {
                "bbox": [np.min(px), np.min(py), np.max(px), np.max(py)],
                "bbox_mode": BoxMode.XYXY_ABS,
                "segmentation": [poly],
                "category_id": category_id,
            }
            if keypoints is not None:
                obj["keypoints"] = keypoints

            objs.append(obj)
        record["annotations"] = objs
        custom_data.append(record)
    return custom_data


def register_dataset(dataset: DataSet,
                     generation_function: Callable = load_custom_data,
                     classes: List[str] = None):
    """Register a custom dataset to the Detectron2 framework.

    Parameters
    ----------
    dataset : DataSet
    generation_function : Callable, optional
        Function, that transforms a given :class:`.DataSet` into a Detectron2
        readable format.\n
        By default :func:`load_custom_data`.
    classes : List[str], optional
        Names of the classes present in the loaded dataset.\n
        By default ``None``, which results in class names like
        ``0, 1, 2, ...``.
    """
    DatasetCatalog.register(dataset.name,
                            lambda: generation_function(dataset))
    if classes is not None:
        MetadataCatalog.get(dataset.name).set(thing_classes=classes)
    else:
        warnings.warn("No thing_classes specified! This will prohibit the use "
                      "of the built-in COCOEvaluator.")


def get_dataset_size(dataset: DataSet) -> int:
    """Compute the number of annotated images in a :class:`.DataSet` (excluding
    augmentation)."""
    with open(dataset.annotation) as metadata:
        annotations = json.load(metadata)
    image_count = 0
    for image in list(annotations.values()):
        # Skip non-annotated image entries
        if image["regions"]:
            image_count += 1
    return image_count


def get_dataset_classes(dataset: DataSet) -> Set[int]:
    """Retrieve the number and IDs of thing classes in the dataset."""
    with open(dataset.annotation) as metadata:
        annotations = json.load(metadata)
    classes = {0, }
    for image in list(annotations.values()):
        regions = image["regions"]
        if regions:
            for region in regions:
                try:
                    classes.add(int(region["region_attributes"]["rod_col"]))
                except KeyError:
                    continue
    return classes
