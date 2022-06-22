# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

from torchdim._C import tree_flatten

def tree_map(fn, tree):
    vs, unflatten = tree_flatten(tree)
    return unflatten(fn(v) for v in vs)
