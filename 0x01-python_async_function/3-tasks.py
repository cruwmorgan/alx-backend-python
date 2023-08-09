#!/usr/bin/env python3
"""Create an asyncio Task"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
        Args:
            max_delay: max wait time

        Return:
            Asyncio Task
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
