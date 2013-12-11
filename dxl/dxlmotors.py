#!/usr/bin/env python


# WINDOWS WARNING: For best performance, parameters of the COM Port should be set to maximum baud rate, and 1ms delay (Device Manager, COM Ports, properties, advanced)

from dxlcore import *
from dxlregisters import *





class DxlMotor(DxlElement):    
    def __init__(self):
        DxlElement.__init__(self)

    def is_motor(self):
        return True
    


    
class DxlMotorAXMX(DxlMotor):
    def __init__(self):
        DxlMotor.__init__(self)

        self.registers["model_number"]=         DxlRegisterWord(0x00,'r',eeprom=True)
        self.registers["firmware"]=             DxlRegisterByte(0x02,'r',eeprom=True)
        self.registers["id"]=                   DxlRegisterByte(0x03,'rw',eeprom=True)
        self.registers["baud_rate"]=            DxlRegisterByte(0x04,'rw',eeprom=True,tosi=self.baud_to_si,fromsi=self.si_to_baud)
        self.registers["return_delay"]=         DxlRegisterByte(0x05,'rw',eeprom=True,tosi=self.pos_to_si,fromsi=self.si_to_pos)
        self.registers["cw_angle_limit"]=       DxlRegisterWord(0x06,'rw',eeprom=True,tosi=self.pos_to_si,fromsi=self.si_to_pos)
        self.registers["ccw_angle_limit"]=      DxlRegisterWord(0x08,'rw',eeprom=True)
        self.registers["high_temp_limit"]=      DxlRegisterByte(0x0b,'rw',eeprom=True)
        self.registers["low_voltage_limit"]=    DxlRegisterByte(0x0c,'rw',eeprom=True)
        self.registers["high_voltage_limit"]=   DxlRegisterByte(0x0d,'rw',eeprom=True)
        self.registers["max_torque"]=           DxlRegisterWord(0x0e,'rw',eeprom=True)
        self.registers["status_return_level"]=  DxlRegisterByte(0x10,'rw',eeprom=True)
        self.registers["alarm_led"]=            DxlRegisterByte(0x11,'rw',eeprom=True)
        self.registers["alarm_shutdown"]=       DxlRegisterByte(0x12,'rw',eeprom=True)

        self.registers["torque_enable"]=        DxlRegisterByte(0x18,'rw',range=[0,1])
        self.registers["led"]=                  DxlRegisterByte(0x19,'rw',range=[0,1])
        
        # Here goes compliance or PID or DIP
        
        self.registers["goal_pos"]=             DxlRegisterWord(0x1E,'rw')
        self.registers["moving_speed"]=         DxlRegisterWord(0x20,'rw')
        self.registers["torque_limit"]=         DxlRegisterWord(0x22,'rw',range=[0,1023])
        self.registers["present_position"]=     DxlRegisterWord(0x24,'r',tosi=self.pos_to_si,fromsi=self.si_to_pos)
        self.registers["present_speed"]=        DxlRegisterWord(0x26,'r')
        self.registers["present_load"]=         DxlRegisterWord(0x28,'r')

        self.registers["present_voltage"]=      DxlRegisterByte(0x2A,'r')
        self.registers["present_temp"]=         DxlRegisterByte(0x2B,'r')
        self.registers["registered"]=           DxlRegisterByte(0x2C,'r')
        self.registers["moving"]=               DxlRegisterByte(0x2E,'r')
        self.registers["lock"]=                 DxlRegisterByte(0x2F,'rw',range=[0,1])
        self.registers["punch"]=                DxlRegisterWord(0x30,'rw',range=[0x20,0x3ff])
        
        self.sort()

    def pos_to_si(self,pos):
        return self.tick_to_rad*float(pos)

    def si_to_pos(self,si):
        return int(float(si)/self.tick_to_rad)        


class DxlMotorAX12(DxlMotorAXMX):
    __metaclass__=ModelRegisteringMetaclass
    model_name="AX12"
    model_number=12
    documentation_url="http://support.robotis.com/en/product/dynamixel/ax_series/dxl_ax_actuator.htm"
    
    tick_to_rad=0.00506145483078355577307870322862
    
    def __init__(self):
        DxlMotorAXMX.__init__(self)

        self.registers["cw_compliance_margin"]= DxlRegisterByte(0x1A,'rw')
        self.registers["ccw_compliance_margin"]=DxlRegisterByte(0x1B,'rw')
        self.registers["cw_compliance_slope"]=  DxlRegisterByte(0x1C,'rw')
        self.registers["ccw_compliance_slope"]= DxlRegisterByte(0x1D,'rw')

        self.registers["goal_pos"]=             DxlRegisterWord(0x1E,'rw',range=[0,1023],tosi=self.pos_to_si,fromsi=self.si_to_pos)
        self.registers["moving_speed"]=         DxlRegisterWord(0x20,'rw',range=[0,1023])

        self.sort()
                
        

class DxlMotorAX18(DxlMotorAXMX):
    __metaclass__=ModelRegisteringMetaclass
    model_name="AX18"
    model_number=18
    documentation_url="http://support.robotis.com/en/product/dynamixel/ax_series/ax-18f.htm"    
    tick_to_rad=0.00506145483078355577307870322862
    
    def __init__(self):
        DxlMotorAXMX.__init__(self)

        self.registers["cw_compliance_margin"]= DxlRegisterByte(0x1A,'rw')
        self.registers["ccw_compliance_margin"]=DxlRegisterByte(0x1B,'rw')
        self.registers["cw_compliance_slope"]=  DxlRegisterByte(0x1C,'rw')
        self.registers["ccw_compliance_slope"]= DxlRegisterByte(0x1D,'rw')

        self.registers["goal_pos"]=             DxlRegisterWord(0x1E,'rw',range=[0,1023],tosi=self.pos_to_si,fromsi=self.si_to_pos)
        self.registers["moving_speed"]=         DxlRegisterWord(0x20,'rw',range=[0,1023])

        self.sort()
                
        

class DxlMotorMX28(DxlMotorAXMX):
    __metaclass__=ModelRegisteringMetaclass
    model_name="MX28"
    model_number=29
    documentation_url="http://support.robotis.com/en/product/dynamixel/rx_series/mx-28.htm"    
    tick_to_rad=0.00153588974175501002769284787627

    def __init__(self):
        DxlMotorAXMX.__init__(self)

        self.registers["p_gain"]=               DxlRegisterByte(0x1A,'rw')
        self.registers["i_gain"]=               DxlRegisterByte(0x1B,'rw')
        self.registers["d_gain"]=               DxlRegisterByte(0x1C,'rw')
        
        self.registers["goal_pos"]=             DxlRegisterWord(0x1E,'rw',range=[0,4096],tosi=self.pos_to_si,fromsi=self.si_to_pos)
        self.registers["moving_speed"]=         DxlRegisterWord(0x20,'rw',range=[0,1023])

        self.sort()

class DxlMotorMX64(DxlMotorAXMX):
    __metaclass__=ModelRegisteringMetaclass
    model_name="MX64"
    model_number=310
    documentation_url="http://support.robotis.com/en/product/dynamixel/mx_series/mx-64.htm"
    tick_to_rad=0.00153588974175501002769284787627

    def __init__(self):
        DxlMotorAXMX.__init__(self)
        
        self.registers["d_gain"]=               DxlRegisterByte(0x1A,'rw')
        self.registers["i_gain"]=               DxlRegisterByte(0x1B,'rw')
        self.registers["p_gain"]=               DxlRegisterByte(0x1C,'rw')

        self.registers["goal_pos"]=             DxlRegisterWord(0x1E,'rw',range=[0,4096],tosi=self.pos_to_si,fromsi=self.si_to_pos)
        self.registers["moving_speed"]=         DxlRegisterWord(0x20,'rw',range=[0,1023])
        
        self.sort()
