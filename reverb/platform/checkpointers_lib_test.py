# Lint as: python3
# Copyright 2019 DeepMind Technologies Limited.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for shared checkpointer utilities."""

from absl.testing import absltest
from reverb import pybind
from reverb.platform import checkpointers_lib


class TempDirCheckpointer(absltest.TestCase):

  def test_constructs_internal_checkpointer(self):
    checkpointer = checkpointers_lib.TempDirCheckpointer()
    self.assertIsInstance(checkpointer.internal_checkpointer(),
                          pybind.Checkpointer)


if __name__ == '__main__':
  absltest.main()
