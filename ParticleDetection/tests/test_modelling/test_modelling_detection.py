# Copyright (c) 2023-24 Adrian Niemann, Dmitry Puzyrev, and others
#
# This file is part of ParticleDetection.
# ParticleDetection is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ParticleDetection is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ParticleDetection. If not, see <http://www.gnu.org/licenses/>.

import sys
from enum import Enum
from types import ModuleType

not_installed = False
try:
    from ParticleDetection.modelling.runners import detection
except ModuleNotFoundError:
    not_installed = True
    # Mock imports of detectron2 modules to allow running of function tests,
    # that don't depend on them.
    module = ModuleType("detectron2")
    module.model_zoo = None
    submod0 = ModuleType("engine")
    submod0.DefaultPredictor = None
    submod1 = ModuleType("utils")
    subsubmod0 = ModuleType("logger")
    subsubmod0.setup_logger = None
    submod2 = ModuleType("config")
    submod2.CfgNode = None
    submod2.get_cfg = None
    submod6 = ModuleType("projects")
    submod6.point_rend = None
    submod7 = ModuleType("export")
    submod7.TracingAdapter = None
    sys.modules["detectron2"] = module
    sys.modules["detectron2.engine"] = submod0
    sys.modules["detectron2.utils"] = submod1
    sys.modules["detectron2.utils.logger"] = subsubmod0
    sys.modules["detectron2.config"] = submod2
    sys.modules["detectron2.projects"] = submod6
    sys.modules["detectron2.export"] = submod7

    module2 = ModuleType("configs")
    module2.write_configs = None
    sys.modules["ParticleDetection.modelling.configs"] = module2

    submod3 = ModuleType("structures")
    submod3.BoxMode = Enum(
        "BoxMode",
        [
            "XYXY_ABS",
        ],
    )
    sys.modules["detectron2.structures"] = submod3
    submod4 = ModuleType("data")
    submod4.DatasetCatalog = None
    submod4.MetadataCatalog = None
    sys.modules["detectron2.data"] = submod4

    submod5 = ModuleType("visualizer")
    submod5.GenericMask = None
    sys.modules["detectron2.utils.visualizer"] = submod5

    submod8 = ModuleType("detection_utils")
    submod8.read_image = None
    sys.modules["detectron2.data.detection_utils"] = submod8
finally:
    from ParticleDetection.modelling.runners import detection  # noqa: F401
