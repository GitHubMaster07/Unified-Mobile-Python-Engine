from pydantic import Field
from pydantic_settings import BaseSettings
from typing import Optional
import yaml

class DeviceSettings(BaseSettings):
    
    platform_name: str = Field(alias="platformName")
    automation_name: str = Field(default="UiAutomator2", alias="automationName")
    device_name: str = Field(alias="deviceName")
    
    
    user_name: Optional[str] = Field(None, alias="userName")
    access_key: Optional[str] = Field(None, alias="accessKey")
    app: Optional[str] = None
    
    
    udid: Optional[str] = None
    app_package: Optional[str] = Field(None, alias="appPackage")
    app_activity: Optional[str] = Field(None, alias="appActivity")
    no_reset: bool = Field(default=True, alias="noReset")

class ConfigLoader:
    @staticmethod
    def load_config(file_path: str = "config/env.yaml") -> DeviceSettings:
        with open(file_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        return DeviceSettings(**data["device"])