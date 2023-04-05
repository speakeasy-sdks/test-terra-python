"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import afibclassificationsample as shared_afibclassificationsample
from ..shared import bloodpressuresample as shared_bloodpressuresample
from ..shared import ecgreading as shared_ecgreading
from ..shared import glucosedatasample as shared_glucosedatasample
from ..shared import heartratedatasample as shared_heartratedatasample
from ..shared import heartratevariabilitydatasamplermssd as shared_heartratevariabilitydatasamplermssd
from ..shared import heartratevariabilitydatasamplesdnn as shared_heartratevariabilitydatasamplesdnn
from ..shared import heartratezone as shared_heartratezone
from ..shared import ketonedatasample as shared_ketonedatasample
from ..shared import measurementdatasample as shared_measurementdatasample
from ..shared import otherdevicedata as shared_otherdevicedata
from ..shared import oxygensaturationsample as shared_oxygensaturationsample
from ..shared import pulsevelocitysample as shared_pulsevelocitysample
from ..shared import temperaturesample as shared_temperaturesample
from ..shared import vo2maxsample as shared_vo2maxsample
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from sdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyBloodPressureData:
    r"""Object containing information on user's Blood Pressure"""
    
    blood_pressure_samples: Optional[list[shared_bloodpressuresample.BloodPressureSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('blood_pressure_samples'), 'exclude': lambda f: f is None }})
    r"""List of Blood Pressure measurements sampled throughout the day"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyDeviceData:
    r"""Object containing information on the device which recorded data for the payload"""
    
    activation_timestamp: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('activation_timestamp'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Activation timestamp of the device, if applicable"""  
    hardware_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hardware_version'), 'exclude': lambda f: f is None }})
    r"""Hardware version of the device"""  
    manufacturer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('manufacturer'), 'exclude': lambda f: f is None }})
    r"""Device manufacturer name"""  
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Device name - note that this can also be the name of the application/package which the data comes from, if coming from a data aggregator such as Google Fit"""  
    other_devices: Optional[list[shared_otherdevicedata.OtherDeviceData]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('other_devices'), 'exclude': lambda f: f is None }})
    r"""Data pertaining to other devices which may have contributed data for this workout"""  
    serial_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('serial_number'), 'exclude': lambda f: f is None }})
    r"""Device Serial Number"""  
    software_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('software_version'), 'exclude': lambda f: f is None }})
    r"""Device Software Version"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyGlucoseData:
    r"""Object containing information on user's blood glucose for the day"""
    
    blood_glucose_samples: Optional[list[shared_glucosedatasample.GlucoseDataSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('blood_glucose_samples'), 'exclude': lambda f: f is None }})
    r"""List of blood glucose readings sampled throughout the day"""  
    day_avg_blood_glucose_mg_per_d_l: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('day_avg_blood_glucose_mg_per_dL'), 'exclude': lambda f: f is None }})
    r"""User's average glucose level throughout the day"""  
    detailed_blood_glucose_samples: Optional[list[shared_glucosedatasample.GlucoseDataSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailed_blood_glucose_samples'), 'exclude': lambda f: f is None }})
    r"""List of blood glucose readings sampled throughout the day - this represents additional data points, potentially at higher frequency from the ones in blood_glucose_samples, which may come at a cost of reduced accuracy"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyHeartDataHeartRateDataDetailed:
    r"""Object containing detailed heart rate information for the associated day"""
    
    hr_samples: Optional[list[shared_heartratedatasample.HeartRateDataSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hr_samples'), 'exclude': lambda f: f is None }})
    r"""Array of HeartRate data samples recorded for the user during the day"""  
    hrv_samples_rmssd: Optional[list[shared_heartratevariabilitydatasamplermssd.HeartRateVariabilityDataSampleRMSSD]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hrv_samples_rmssd'), 'exclude': lambda f: f is None }})
    r"""Array of HeartRate Variability data samples recorded for the user during the day, computed using RMSSD"""  
    hrv_samples_sdnn: Optional[list[shared_heartratevariabilitydatasamplesdnn.HeartRateVariabilityDataSampleSDNN]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hrv_samples_sdnn'), 'exclude': lambda f: f is None }})
    r"""Array of HeartRate Variability data samples recorded for the user during the day, computed using SDNN"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyHeartDataHeartRateDataSummary:
    r"""Object containing summary information for the associated day"""
    
    avg_hr_bpm: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avg_hr_bpm'), 'exclude': lambda f: f is None }})
    r"""Average HeartRate of the user during the day"""  
    avg_hrv_rmssd: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avg_hrv_rmssd'), 'exclude': lambda f: f is None }})
    r"""Average HeartRate Variability of the user during the day, computed using RMSSD"""  
    avg_hrv_sdnn: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avg_hrv_sdnn'), 'exclude': lambda f: f is None }})
    r"""Average HeartRate Variability of the user during the day, computed using SDNN"""  
    hr_zone_data: Optional[list[shared_heartratezone.HeartRateZone]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hr_zone_data'), 'exclude': lambda f: f is None }})
    r"""Array of time spent in various HR zones throughout the day"""  
    max_hr_bpm: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('max_hr_bpm'), 'exclude': lambda f: f is None }})
    r"""Maximum HeartRate of the user during the day"""  
    min_hr_bpm: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('min_hr_bpm'), 'exclude': lambda f: f is None }})
    r"""Minimum HeartRate of the user during the day"""  
    resting_hr_bpm: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resting_hr_bpm'), 'exclude': lambda f: f is None }})
    r"""Resting HeartRate of the user, as determined by the fitness data provider"""  
    user_max_hr_bpm: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_max_hr_bpm'), 'exclude': lambda f: f is None }})
    r"""User's maximum HeartRate based on their age, and other factors as determined by the fitness data provider"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyHeartDataHeartRateData:
    
    detailed: Optional[BodyHeartDataHeartRateDataDetailed] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('detailed'), 'exclude': lambda f: f is None }})
    r"""Object containing detailed heart rate information for the associated day"""  
    summary: Optional[BodyHeartDataHeartRateDataSummary] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary'), 'exclude': lambda f: f is None }})
    r"""Object containing summary information for the associated day"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyHeartData:
    r"""Object containing information on user's heart metrics"""
    
    afib_classification_samples: Optional[list[shared_afibclassificationsample.AFibClassificationSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('afib_classification_samples'), 'exclude': lambda f: f is None }})
    r"""List of Atrial Fibrillation classification measurements sampled through the day."""  
    ecg_signal: Optional[list[shared_ecgreading.ECGReading]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecg_signal'), 'exclude': lambda f: f is None }})
    r"""List of ECGReadings sampled through the day."""  
    heart_rate_data: Optional[BodyHeartDataHeartRateData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('heart_rate_data'), 'exclude': lambda f: f is None }})  
    pulse_wave_velocity_samples: Optional[list[shared_pulsevelocitysample.PulseVelocitySample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pulse_wave_velocity_samples'), 'exclude': lambda f: f is None }})
    r"""List of Pulse Wave Velocity measurements sampled throughout the day. This represents a measurement of arterial stiffness that is an independent predictor of cardiovascular risk"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyHydrationData:
    r"""Object containing information on user's hydration (both internal & consumption of water) for the day"""
    
    day_total_water_consumption_ml: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('day_total_water_consumption_ml'), 'exclude': lambda f: f is None }})
    r"""User's total water consumption throughout the day"""  
    hydration_amount_samples: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hydration_amount_samples'), 'exclude': lambda f: f is None }})
    r"""User's body water content"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyKetoneData:
    r"""Object containing information on user's ketone data for the day"""
    
    ketone_samples: Optional[list[shared_ketonedatasample.KetoneDataSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ketone_samples'), 'exclude': lambda f: f is None }})
    r"""List of ketone data sampled through the day."""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyMeasurementsData:
    r"""Object containing information on body measurements for the day"""
    
    measurements: Optional[list[shared_measurementdatasample.MeasurementDataSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('measurements'), 'exclude': lambda f: f is None }})
    r"""List of body metrics & measurements taken throughout the associated day"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyMetadata:
    r"""Object containing daily summary metadata"""
    
    end_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The end time of the associated day, in ISO8601 format with microsecond precision. Will always fall on midnight of any given day, and will always be equal to 24h after start_time. TimeZone info will be provided whenever possible. If absent, the time corresponds to the user's local time"""  
    start_time: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_time'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The start time of the associated day, in ISO8601 format with microsecond precision. Will always fall on midnight of any given day, and will always be equal to 24h before end_time. TimeZone info will be provided whenever possible. If absent, the time corresponds to the user's local time"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyOxygenData:
    r"""Object containing information on user's oxygen-related data"""
    
    avg_saturation_percentage: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('avg_saturation_percentage'), 'exclude': lambda f: f is None }})
    r"""Average Oxygen Saturation percentage of the user during the workout (SpO2 or SmO2)"""  
    saturation_samples: Optional[list[shared_oxygensaturationsample.OxygenSaturationSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('saturation_samples'), 'exclude': lambda f: f is None }})
    r"""Array of Oxygen Saturation percentage datapoints sampled throughout the workout"""  
    vo2_samples: Optional[list[shared_vo2maxsample.Vo2MaxSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vo2_samples'), 'exclude': lambda f: f is None }})
    r"""Array of VO2 datapoints sampled throughout the workout"""  
    vo2max_ml_per_min_per_kg: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vo2max_ml_per_min_per_kg'), 'exclude': lambda f: f is None }})
    r"""VO2Max for the given user"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BodyTemperatureData:
    r"""Object containing temperature information (core, skin, ambient) during the day"""
    
    ambient_temperature_samples: Optional[list[shared_temperaturesample.TemperatureSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ambient_temperature_samples'), 'exclude': lambda f: f is None }})
    r"""List of ambient temperature measurements sampled throughout the day"""  
    body_temperature_samples: Optional[list[shared_temperaturesample.TemperatureSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body_temperature_samples'), 'exclude': lambda f: f is None }})
    r"""List of body temperature measurements sampled throughout the day"""  
    skin_temperature_samples: Optional[list[shared_temperaturesample.TemperatureSample]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skin_temperature_samples'), 'exclude': lambda f: f is None }})
    r"""List of skin temperature measurements sampled throughout the day"""  
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Body:
    
    blood_pressure_data: Optional[BodyBloodPressureData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('blood_pressure_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on user's Blood Pressure"""  
    device_data: Optional[BodyDeviceData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('device_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on the device which recorded data for the payload"""  
    glucose_data: Optional[BodyGlucoseData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('glucose_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on user's blood glucose for the day"""  
    heart_data: Optional[BodyHeartData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('heart_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on user's heart metrics"""  
    hydration_data: Optional[BodyHydrationData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hydration_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on user's hydration (both internal & consumption of water) for the day"""  
    ketone_data: Optional[BodyKetoneData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ketone_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on user's ketone data for the day"""  
    measurements_data: Optional[BodyMeasurementsData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('measurements_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on body measurements for the day"""  
    metadata: Optional[BodyMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    r"""Object containing daily summary metadata"""  
    oxygen_data: Optional[BodyOxygenData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('oxygen_data'), 'exclude': lambda f: f is None }})
    r"""Object containing information on user's oxygen-related data"""  
    temperature_data: Optional[BodyTemperatureData] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('temperature_data'), 'exclude': lambda f: f is None }})
    r"""Object containing temperature information (core, skin, ambient) during the day"""  
    