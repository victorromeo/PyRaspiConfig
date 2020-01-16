# -*- coding: utf-8 -*-
import subprocess
import shlex
from typing import List

class PyRaspiConfig:
    """PyRaspiConfig"""

    @classmethod
    def _ExecuteCmd(self, command):
        return self._Execute(shlex.split('sudo raspi-config nonint {0}'.format(command)))

    @classmethod
    def _Execute(self, command:List[str]):
        """Executes a command in a consistent way"""
        process = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        process
        return process.stdout.decode("utf-8"), process.stderr.decode("utf-8")

    @classmethod
    def GetCanExpand(self) -> bool:
        """Gets a flag indicating if the filesystem takes up the entire disk"""
        out,err = self._ExecuteCmd('get_can_expand')

        return out, err

    @classmethod
    def GetHostname(self) -> str:
        out,err = self._ExecuteCmd('get_hostname')

        return out, err

#define GET_CAN_EXPAND  "sudo raspi-config nonint get_can_expand"
#define EXPAND_FS       "sudo raspi-config nonint do_expand_rootfs"
#define GET_HOSTNAME    "sudo raspi-config nonint get_hostname"
#define SET_HOSTNAME    "sudo raspi-config nonint do_hostname %s"
#define GET_BOOT_CLI    "sudo raspi-config nonint get_boot_cli"
#define GET_AUTOLOGIN   "sudo raspi-config nonint get_autologin"
#define SET_BOOT_CLI    "sudo raspi-config nonint do_boot_behaviour B1"
#define SET_BOOT_CLIA   "sudo raspi-config nonint do_boot_behaviour B2"
#define SET_BOOT_GUI    "sudo raspi-config nonint do_boot_behaviour B3"
#define SET_BOOT_GUIA   "sudo raspi-config nonint do_boot_behaviour B4"
#define GET_BOOT_WAIT   "sudo raspi-config nonint get_boot_wait"
#define SET_BOOT_WAIT   "sudo raspi-config nonint do_boot_wait %d"
#define GET_SPLASH      "sudo raspi-config nonint get_boot_splash"
#define SET_SPLASH      "sudo raspi-config nonint do_boot_splash %d"
#define GET_OVERSCAN    "sudo raspi-config nonint get_overscan"
#define SET_OVERSCAN    "sudo raspi-config nonint do_overscan %d"
#define GET_CAMERA      "sudo raspi-config nonint get_camera"
#define SET_CAMERA      "sudo raspi-config nonint do_camera %d"
#define GET_SSH         "sudo raspi-config nonint get_ssh"
#define SET_SSH         "sudo raspi-config nonint do_ssh %d"
#define GET_VNC         "sudo raspi-config nonint get_vnc"
#define SET_VNC         "sudo raspi-config nonint do_vnc %d"
#define GET_SPI         "sudo raspi-config nonint get_spi"
#define SET_SPI         "sudo raspi-config nonint do_spi %d"
#define GET_I2C         "sudo raspi-config nonint get_i2c"
#define SET_I2C         "sudo raspi-config nonint do_i2c %d"
#define GET_SERIAL      "sudo raspi-config nonint get_serial"
#define GET_SERIALHW    "sudo raspi-config nonint get_serial_hw"
#define SET_SERIAL      "sudo raspi-config nonint do_serial %d"
#define GET_1WIRE       "sudo raspi-config nonint get_onewire"
#define SET_1WIRE       "sudo raspi-config nonint do_onewire %d"
#define GET_RGPIO       "sudo raspi-config nonint get_rgpio"
#define SET_RGPIO       "sudo raspi-config nonint do_rgpio %d"
#define GET_PI_TYPE     "sudo raspi-config nonint get_pi_type"
#define GET_OVERCLOCK   "sudo raspi-config nonint get_config_var arm_freq /boot/config.txt"
#define SET_OVERCLOCK   "sudo raspi-config nonint do_overclock %s"
#define GET_GPU_MEM     "sudo raspi-config nonint get_config_var gpu_mem /boot/config.txt"
#define GET_GPU_MEM_256 "sudo raspi-config nonint get_config_var gpu_mem_256 /boot/config.txt"
#define GET_GPU_MEM_512 "sudo raspi-config nonint get_config_var gpu_mem_512 /boot/config.txt"
#define GET_GPU_MEM_1K  "sudo raspi-config nonint get_config_var gpu_mem_1024 /boot/config.txt"
#define SET_GPU_MEM     "sudo raspi-config nonint do_memory_split %d"
#define GET_HDMI_GROUP  "sudo raspi-config nonint get_config_var hdmi_group /boot/config.txt"
#define GET_HDMI_MODE   "sudo raspi-config nonint get_config_var hdmi_mode /boot/config.txt"
#define SET_HDMI_GP_MOD "sudo raspi-config nonint do_resolution %d %d"
#define GET_WIFI_CTRY   "sudo raspi-config nonint get_wifi_country"
#define SET_WIFI_CTRY   "sudo raspi-config nonint do_wifi_country %s"
#define CHANGE_PASSWD   "(echo \"%s\" ; echo \"%s\" ; echo \"%s\") | passwd"
