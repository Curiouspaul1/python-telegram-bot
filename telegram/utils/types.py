#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2020
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""This module contains custom typing aliases."""
from pathlib import Path
from typing import IO, TYPE_CHECKING, Any, Dict, List, Optional, Tuple, TypeVar, Union

if TYPE_CHECKING:
    from telegram import InputFile, Update

FileLike = Union[IO, 'InputFile']
"""Either an open file handler or a :class:`telegram.InputFile`."""

FileInput = Union[str, bytes, FileLike, Path]
"""Valid input for passing files to Telegram. Either a file id as string, a file like object,
a local file path as string, :class:`pathlib.Path` or the file contents as :obj:`bytes`."""

JSONDict = Dict[str, Any]
"""Dictionary containing response from Telegram or data to send to the API."""

HandlerArg = Union[str, 'Update']
"""The argument that handlers parse for :meth:`telegram.ext.handler.check_update` etc."""

ConversationDict = Dict[Tuple[int, ...], Optional[object]]
"""Dicts as maintained by the :class:`telegram.ext.ConversationHandler`."""

RT = TypeVar("RT")
SLT = Union[RT, List[RT], Tuple[RT, ...]]
"""Single instance or list/tuple of instances."""
