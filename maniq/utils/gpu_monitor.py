#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GPU monitoring utilities for Maniq
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)


class GPUMonitor:
    """Monitor GPU usage during testing"""
    
    def __init__(self):
        self.nvml_available = False
        self.handle = None
        
        try:
            import pynvml
            pynvml.nvmlInit()
            self.nvml_available = True
            # Get first GPU handle
            device_count = pynvml.nvmlDeviceGetCount()
            if device_count > 0:
                self.handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            else:
                logger.warning("No GPU devices found")
                self.nvml_available = False
        except ImportError:
            logger.warning("pynvml not available, GPU monitoring disabled")
        except Exception as e:
            logger.warning(f"Failed to initialize NVML: {e}")
            self.nvml_available = False
    
    def get_gpu_usage(self) -> float:
        """Get current GPU usage percentage"""
        if not self.nvml_available or self.handle is None:
            return 0.0
        
        try:
            import pynvml
            util = pynvml.nvmlDeviceGetUtilizationRates(self.handle)
            return float(util.gpu)
        except Exception as e:
            logger.warning(f"Failed to get GPU usage: {e}")
            return 0.0
    
    def get_gpu_info(self) -> str:
        """Get GPU information string"""
        if not self.nvml_available or self.handle is None:
            return "Unknown GPU"
        
        try:
            import pynvml
            name = pynvml.nvmlDeviceGetName(self.handle)
            if isinstance(name, bytes):
                name = name.decode('utf-8')
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(self.handle)
            total_memory_gb = memory_info.total / (1024**3)
            return f"{name} ({total_memory_gb:.1f} GB)"
        except Exception as e:
            logger.warning(f"Failed to get GPU info: {e}")
            return "Unknown GPU"
    
    def cleanup(self):
        """Cleanup NVML resources"""
        if self.nvml_available:
            try:
                import pynvml
                pynvml.nvmlShutdown()
            except Exception:
                pass
                