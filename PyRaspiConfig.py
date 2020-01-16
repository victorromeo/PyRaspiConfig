# -*- coding: utf-8 -*-
import subprocess
import shlex
from crypt import crypt
from getpass import getpass
from typing import List, Tuple

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
    def GetCanExpand(self) -> Tuple[bool,str]:
        """Gets a flag indicating if the filesystem takes up the entire disk"""
        out,err = self._ExecuteCmd('get_can_expand')

        return bool(int(out)), err


    @classmethod
    def ExpandRootFS(self) -> Tuple[str, str]:
        """Make the filesystem take up the entire disk"""
        out,err = self._ExecuteCmd('do_expand_rootfs')

        return out, err

    @classmethod
    def GetHostname(self) -> Tuple[str,str]:
        """Get the hostname"""
        out,err = self._ExecuteCmd('get_hostname')

        return out, err

    @classmethod
    def SetHostname(self, hostname) -> Tuple[str,str]:
        """Sets the hostname"""
        out,err = self._ExecuteCmd('do_hostname {0}'.format(hostname))

        return out, err

    @classmethod
    def GetBootCLI(self) -> Tuple[bool,str]:
        out,err = self._ExecuteCmd('get_boot_cli')

        return bool(int(out)), err

    @classmethod
    def GetAutoLogin(self) -> Tuple[bool,str]:
        out,err = self._ExecuteCmd('get_autologin')

        return bool(int(out)), err

    @classmethod
    def SetBootCLI(self) -> Tuple[str,str]:
        """Make the host boot to the command prompt"""
        out,err = self._ExecuteCmd('do_boot_behaviour B1')

        return out, err

    @classmethod
    def SetBootCLIA(self) -> Tuple[str,str]:
        """Make the host boot to the command prompt with AutoLogin as 'pi'"""
        out,err = self._ExecuteCmd('do_boot_behaviour B2')

        return out, err

    @classmethod
    def SetBootGUI(self) -> Tuple[str,str]:
        """Make the host boot to the GUI"""
        out,err = self._ExecuteCmd('do_boot_behaviour B3')

        return out, err

    @classmethod
    def SetBootGUIA(self) -> Tuple[str,str]:
        """Make the host boot to the GUI with AutoLogin as 'pi'"""
        out,err = self._ExecuteCmd('do_boot_behaviour B4')

        return out, err

    @classmethod
    def GetBootWait(self) -> Tuple[bool,str]:
        """Get the boot wait for network"""
        out,err = self._ExecuteCmd('get_boot_wait')

        return bool(int(out)), err

    @classmethod
    def SetBootWait(self, enable:bool):
        """Set the boot wait for network"""
        out,err = self._ExecuteCmd('set_boot_wait {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetBootSplash(self) -> Tuple[bool,str]:
        """Get the boot splash enable state"""
        out,err = self._ExecuteCmd('get_boot_splash')

        return bool(int(out)), err

    @classmethod
    def SetBootSplash(self, enable: bool) -> Tuple[bool,str]:
        """Set the boot splash enable state"""
        out,err = self._ExecuteCmd('do_boot_splash {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetOverscan(self) -> Tuple[bool,str]:
        """Get the Screen overscan mode"""
        out,err = self._ExecuteCmd('get_overscan')

        return bool(int(out)), err

    @classmethod
    def SetOverscan(self, enable: bool) -> Tuple[bool,str]:
        """Set the Screen overscan to remove black bars"""
        out,err = self._ExecuteCmd('do_overscan {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetCamera(self) -> Tuple[bool,str]:
        """Get the Camera enable state"""
        out,err = self._ExecuteCmd('get_camera')

        return bool(int(out)), err

    @classmethod
    def SetCamera(self, enable: bool) -> Tuple[bool,str]:
        """Set the Camera enable state"""
        out,err = self._ExecuteCmd('do_camera {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetSSH(self) -> Tuple[bool,str]:
        """Get the SSH enable state"""
        out,err = self._ExecuteCmd('get_camera')

        return bool(int(out)), err

    @classmethod
    def SetSSH(self, enable: bool) -> Tuple[bool,str]:
        """Set the SSH enable state"""
        out,err = self._ExecuteCmd('do_camera {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetVNC(self) -> Tuple[bool,str]:
        """Get the VNC Server enable state"""
        out,err = self._ExecuteCmd('get_vnc')

        return bool(int(out)), err

    @classmethod
    def SetVNC(self, enable: bool) -> Tuple[bool,str]:
        """Set the VNC Server enable state"""
        out,err = self._ExecuteCmd('do_vnc {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetSPI(self) -> Tuple[bool,str]:
        """Get the SPI enable state"""
        out,err = self._ExecuteCmd('get_spi')

        return bool(int(out)), err

    @classmethod
    def SetSPI(self, enable: bool) -> Tuple[bool,str]:
        """Set the SPI enable state"""
        out,err = self._ExecuteCmd('do_spi {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetI2C(self) -> Tuple[bool,str]:
        """Get the I2C enable state"""
        out,err = self._ExecuteCmd('get_i2c')

        return bool(int(out)), err

    @classmethod
    def SetI2C(self, enable: bool) -> Tuple[bool,str]:
        """Set the I2C enable state"""
        out,err = self._ExecuteCmd('do_i2c {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetSerial(self) -> Tuple[bool,str]:
        """Get the Login shell over serial enable state"""
        out,err = self._ExecuteCmd('get_serial')

        return bool(int(out)), err

    @classmethod
    def GetSerialHW(self) -> Tuple[bool,str]:
        """Get Serial Hardware Port enable state"""
        out,err = self._ExecuteCmd('get_serial_hw')

        return bool(int(out)), err

    @classmethod
    def SetSerial(self, enable: bool) -> Tuple[bool,str]:
        """Set the Login shell over serial enable state"""
        out,err = self._ExecuteCmd('do_serial {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetoneWire(self) -> Tuple[bool,str]:
        """Get the One Wire enable state"""
        out,err = self._ExecuteCmd('get_onewire')

        return bool(int(out)), err

    @classmethod
    def SetOneWire(self, enable: bool) -> Tuple[bool,str]:
        """Set the One Wire enable state"""
        out,err = self._ExecuteCmd('do_onewire {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetRemoteGPIO(self) -> Tuple[bool,str]:
        """Get the Remote GPIO enable state"""
        out,err = self._ExecuteCmd('get_rgpio')

        return bool(int(out)), err

    @classmethod
    def SetRemoteGPIO(self, enable: bool) -> Tuple[bool,str]:
        """Set the Remote GPIO enable state"""
        out,err = self._ExecuteCmd('do_rgpio {0}'.format(int(enable)))

        return out, err

    @classmethod
    def GetPIType(self) -> Tuple[bool,str]:
        """Get the PI Type"""
        out,err = self._ExecuteCmd('get_pi_type')

        return bool(int(out)), err

    @classmethod
    def GetOverclock(self) -> Tuple[bool,str]:
        """Get the Overclock enable state"""
        out,err = self._ExecuteCmd('get_config_var arm_freq /boot/config.txt')

        return bool(int(out)), err

    @classmethod
    def SetOverclock(self, overclock: str) -> Tuple[bool,str]:
        """Set the Overclock enable state"""
        out,err = self._ExecuteCmd('do_overclock {0}'.format(overclock))

        return out, err

    @classmethod
    def GetGPUMemory(self) -> Tuple[int,str]:
        """Get the GPU Memory"""
        out,err = self._ExecuteCmd('get_config_var gpu_mem /boot/config.txt')

        return int(out), err

    @classmethod
    def GetGPUMemory256(self) -> Tuple[int,str]:
        """Get the GPU Memory"""
        out,err = self._ExecuteCmd('get_config_var gpu_mem_256 /boot/config.txt')

        return int(out), err

    @classmethod
    def GetGPUMemory512(self) -> Tuple[int,str]:
        """Get the GPU Memory"""
        out,err = self._ExecuteCmd('get_config_var gpu_mem_512 /boot/config.txt')

        return int(out), err

    @classmethod
    def GetGPUMemory1024(self) -> Tuple[int,str]:
        """Get the GPU Memory"""
        out,err = self._ExecuteCmd('get_config_var gpu_mem_1024 /boot/config.txt')

        return int(out), err

    @classmethod
    def SetGPUMemory(self, memory:int) -> Tuple[str,str]:
        """Set the GPU Memory"""
        out,err = self._ExecuteCmd('do_memory_split {0}'.format(memory))

        return out, err

    @classmethod
    def GetHDMIGroup(self) -> Tuple[int,str]:
        """Get the HDMI Group"""
        out,err = self._ExecuteCmd('get_config_var hdmi_group /boot/config.txt')

        return int(out), err

    @classmethod
    def GetHDMIMode(self) -> Tuple[int,str]:
        """Get the HDMI Mode"""
        out,err = self._ExecuteCmd('get_config_var hdmi_mode /boot/config.txt')

        return int(out), err

    @classmethod
    def SetHDMIGroupMode(self, group: int, mode: int) -> Tuple[str,str]:
        """Set the HDMI Group and Mode"""
        out,err = self._ExecuteCmd('do_resolution {0} {1}'.format(group, mode))

        return out, err

    @classmethod
    def GetWiFiCountry(self) -> Tuple[str,str]:
        """Get the WiFi country code"""
        out,err = self._ExecuteCmd('get_wifi_country')

        return out, err

    @classmethod
    def SetWiFiCountry(self, country_code: str) -> Tuple[bool,str]:
        """Set the  enable state"""
        out,err = self._ExecuteCmd('do_wifi_country {0}'.format(country_code))

        return out, err

    @classmethod
    def SetPassword(self,username:str, password:str):
        """Set the password (Not Secure)"""
        process = subprocess.Popen(['/usr/bin/sudo', '/usr/sbin/chpasswd' ], universal_newlines=True, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (stdout, stderr) = process.communicate(username + ":" + password + "\n")
        assert process.wait() == 0
        if stdout or stderr:
            raise Exception("Error encountered changing the password!")