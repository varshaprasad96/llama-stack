# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.


from typing import Any, Literal

from pydantic import BaseModel

from llama_stack.schema_utils import json_schema_type


@json_schema_type
class QdrantVectorIOConfig(BaseModel):
    path: str
    distance_metric: Literal["COSINE", "DOT", "EUCLID", "MANHATTAN"] = "COSINE"

    @classmethod
    def sample_run_config(cls, __distro_dir__: str) -> dict[str, Any]:
        return {
            "path": "${env.QDRANT_PATH:=~/.llama/" + __distro_dir__ + "}/" + "qdrant.db",
        }
