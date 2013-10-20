#!/usr/bin/python
#coding=utf8

pids = [
('01','00','4','PIDs supported [01 - 20]','','','','Bit encoded [A7..D0] == [PID $01..PID $20] <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','01','4','Monitor status since DTCs cleared. (Includes malfunction indicator lamp (MIL) status and number of DTCs.)','','','','Bit encoded. <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','02','2','Freeze <a href="/wiki/Diagnostic_Trouble_Code" title="Diagnostic Trouble Code" class="mw-redirect">DTC</a>','','','',''),
('01','03','2','Fuel system status','','','','Bit encoded. <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','04','1','Calculated engine load value','0','100','&#160;%','A*100/255'),
('01','05','1','Engine coolant temperature','-40','215','degree C','A-40'),
('01','06','1','Short term fuel&#160;% trim—Bank 1','-100 Subtracting Fuel (Rich Condition)','99.22 Adding Fuel (Lean Condition)','&#160;%','(A-128) * 100/128'),
('01','07','1','Long term fuel&#160;% trim—Bank 1','-100 Subtracting Fuel (Rich Condition)','99.22 Adding Fuel (Lean Condition)','&#160;%','(A-128) * 100/128'),
('01','08','1','Short term fuel&#160;% trim—Bank 2','-100 Subtracting Fuel (Rich Condition)','99.22 Adding Fuel (Lean Condition)','&#160;%','(A-128) * 100/128'),
('01','09','1','Long term fuel&#160;% trim—Bank 2','-100 Subtracting Fuel (Rich Condition)','99.22 Adding Fuel (Lean Condition)','&#160;%','(A-128) * 100/128'),
('01','0A','1','Fuel pressure','0','765','kPa (gauge)','A*3'),
('01','0B','1','Intake manifold absolute pressure','0','255','kPa (absolute)','A'),
('01','0C','2','Engine RPM','0','16,383.75','rpm','((A*256)+B)/4'),
('01','0D','1','Vehicle speed','0','255','km/h','A'),
('01','0E','1','Timing advance','-64','63.5','° relative to #1 cylinder','A/2 - 64'),
('01','0F','1','Intake air temperature','-40','215','°C','A-40'),
('01','10','2','MAF air flow rate','0','655.35','grams/sec','((A*256)+B) / 100'),
('01','11','1','Throttle position','0','100','&#160;%','A*100/255'),
('01','12','1','Commanded secondary air status','','','','Bit encoded. <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','13','1','Oxygen sensors present','','','','[A0..A3] == Bank 1, Sensors 1-4. [A4..A7] == Bank 2...'),
('01','14','2','Bank 1, Sensor 1:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','15','2','Bank 1, Sensor 2:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','16','2','Bank 1, Sensor 3:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','17','2','Bank 1, Sensor 4:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','18','2','Bank 2, Sensor 1:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','19','2','Bank 2, Sensor 2:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','1A','2','Bank 2, Sensor 3:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','1B','2','Bank 2, Sensor 4:Oxygen sensor voltage,Short term fuel trim','0-100(lean)','1.27599.2(rich)','Volts%','A/200(B-128) * 100/128 (if B==$FF, sensor is not used in trim calc)'),
('01','1C','1','OBD standards this vehicle conforms to','','','','Bit encoded. <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','1D','1','Oxygen sensors present','','','','Similar to PID 13, but [A0..A7] == [B1S1, B1S2, B2S1, B2S2, B3S1, B3S2, B4S1, B4S2]'),
('01','1E','1','Auxiliary input status','','','','A0 == Power Take Off (PTO) status (1 == active)[A1..A7] not used'),
('01','1F','2','Run time since engine start','0','65,535','seconds','(A*256)+B'),
('01','20','4','PIDs supported [21 - 40]','','','','Bit encoded [A7..D0] == [PID $21..PID $40] <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','21','2','Distance traveled with malfunction indicator lamp (MIL) on','0','65,535','km','(A*256)+B'),
('01','22','2','Fuel Rail Pressure (relative to manifold vacuum)','0','5177.265','kPa','((A*256)+B) * 0.079'),
('01','23','2','Fuel Rail Pressure (diesel, or gasoline direct inject)','0','655,350','kPa (gauge)','((A*256)+B) * 10'),
('01','24','4','O2S1_WR_lambda(1):Equivalence RatioVoltage','00','1.9997.999','N/AV','((A*256)+B)*2/65535 or ((A*256)+B)/32768((C*256)+D)*8/65535 or ((C*256)+D)/8192'),
('01','25','4','O2S2_WR_lambda(1):Equivalence RatioVoltage','00','28','N/AV','((A*256)+B)*2/65535((C*256)+D)*8/65535'),
('01','26','4','O2S3_WR_lambda(1):Equivalence RatioVoltage','00','28','N/AV','((A*256)+B)*2/65535((C*256)+D)*8/65535'),
('01','27','4','O2S4_WR_lambda(1):Equivalence RatioVoltage','00','28','N/AV','((A*256)+B)*2/65535((C*256)+D)*8/65535'),
('01','28','4','O2S5_WR_lambda(1):Equivalence RatioVoltage','00','28','N/AV','((A*256)+B)*2/65535((C*256)+D)*8/65535'),
('01','29','4','O2S6_WR_lambda(1):Equivalence RatioVoltage','00','28','N/AV','((A*256)+B)*2/65535((C*256)+D)*8/65535'),
('01','2A','4','O2S7_WR_lambda(1):Equivalence RatioVoltage','00','28','N/AV','((A*256)+B)*2/65535((C*256)+D)*8/65535'),
('01','2B','4','O2S8_WR_lambda(1):Equivalence RatioVoltage','00','28','N/AV','((A*256)+B)*2/65535((C*256)+D)*8/65535'),
('01','2C','1','Commanded EGR','0','100','&#160;%','A*100/255'),
('01','2D','1','EGR Error','-100','99.22','&#160;%','(A-128) * 100/128'),
('01','2E','1','Commanded evaporative purge','0','100','&#160;%','A*100/255'),
('01','2F','1','Fuel Level Input','0','100','&#160;%','A*100/255'),
('01','30','1','# of warm-ups since codes cleared','0','255','N/A','A'),
('01','31','2','Distance traveled since codes cleared','0','65,535','km','(A*256)+B'),
('01','32','2','Evap. System Vapor Pressure','-8,192','8,192','Pa','((A*256)+B)/4 (A and B are <a href="/wiki/Two%27s_complement" title="Two\'s complement">two\'s complement</a> signed)'),
('01','33','1','Barometric pressure','0','255','kPa (Absolute)','A'),
('01','34','4','O2S1_WR_lambda(1):Equivalence RatioCurrent','0-128','1.999127.99','N/AmA','((A*256)+B)/32,768((C*256)+D)/256 - 128'),
('01','35','4','O2S2_WR_lambda(1):Equivalence RatioCurrent','0-128','2128','N/AmA','((A*256)+B)/32,768((C*256)+D)/256 - 128'),
('01','36','4','O2S3_WR_lambda(1):Equivalence RatioCurrent','0-128','2128','N/AmA','((A*256)+B)/32768((C*256)+D)/256 - 128'),
('01','37','4','O2S4_WR_lambda(1):Equivalence RatioCurrent','0-128','2128','N/AmA','((A*256)+B)/32,768((C*256)+D)/256 - 128'),
('01','38','4','O2S5_WR_lambda(1):Equivalence RatioCurrent','0-128','2128','N/AmA','((A*256)+B)/32,768((C*256)+D)/256 - 128'),
('01','39','4','O2S6_WR_lambda(1):Equivalence RatioCurrent','0-128','2128','N/AmA','((A*256)+B)/32,768((C*256)+D)/256 - 128'),
('01','3A','4','O2S7_WR_lambda(1):Equivalence RatioCurrent','0-128','2128','N/AmA','((A*256)+B)/32,768((C*256)+D)/256 - 128'),
('01','3B','4','O2S8_WR_lambda(1):Equivalence RatioCurrent','0-128','2128','N/AmA','((A*256)+B)/32,768((C*256)+D)/256 - 128'),
('01','3C','2','Catalyst TemperatureBank 1, Sensor 1','-40','6,513.5','°C','((A*256)+B)/10 - 40'),
('01','3D','2','Catalyst TemperatureBank 2, Sensor 1','-40','6,513.5','°C','((A*256)+B)/10 - 40'),
('01','3E','2','Catalyst TemperatureBank 1, Sensor 2','-40','6,513.5','°C','((A*256)+B)/10 - 40'),
('01','3F','2','Catalyst TemperatureBank 2, Sensor 2','-40','6,513.5','°C','((A*256)+B)/10 - 40'),
('01','40','4','PIDs supported [41 - 60]','','','','Bit encoded [A7..D0] == [PID $41..PID $60] <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','41','4','Monitor status this drive cycle','','','','Bit encoded. <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','42','2','Control module voltage','0','65.535','V','((A*256)+B)/1000'),
('01','43','2','Absolute load value','0','25,700','&#160;%','((A*256)+B)*100/255'),
('01','44','2','Command equivalence ratio','0','2','N/A','((A*256)+B)/32768'),
('01','45','1','Relative throttle position','0','100','&#160;%','A*100/255'),
('01','46','1','Ambient air temperature','-40','215','°C','A-40'),
('01','47','1','Absolute throttle position B','0','100','&#160;%','A*100/255'),
('01','48','1','Absolute throttle position C','0','100','&#160;%','A*100/255'),
('01','49','1','Accelerator pedal position D','0','100','&#160;%','A*100/255'),
('01','4A','1','Accelerator pedal position E','0','100','&#160;%','A*100/255'),
('01','4B','1','Accelerator pedal position F','0','100','&#160;%','A*100/255'),
('01','4C','1','Commanded throttle actuator','0','100','&#160;%','A*100/255'),
('01','4D','2','Time run with MIL on','0','65,535','minutes','(A*256)+B'),
('01','4E','2','Time since trouble codes cleared','0','65,535','minutes','(A*256)+B'),
('01','4F','4','Maximum value for equivalence ratio, oxygen sensor voltage, oxygen sensor current, and intake manifold absolute pressure','0, 0, 0, 0','255, 255, 255, 2550',', V, mA, kPa','A, B, C, D*10'),
('01','50','4','Maximum value for air flow rate from mass air flow sensor','0','2550','g/s','A*10, B, C, and D are reserved for future use'),
('01','51','1','Fuel Type','','','','From fuel type table <a href="#Fuel_Type_Coding">see below</a>'),
('01','52','1','Ethanol fuel&#160;%','0','100','&#160;%','A*100/255'),
('01','53','2','Absolute Evap system Vapor Pressure','0','327.675','kPa','((A*256)+B)/200'),
('01','54','2','Evap system vapor pressure','-32,767','32,768','Pa','((A*256)+B)-32767'),
('01','55','2','Short term secondary oxygen sensor trim bank 1 and bank 3','-100','99.22','&#160;%','(A-128)*100/128(B-128)*100/128'),
('01','56','2','Long term secondary oxygen sensor trim bank 1 and bank 3','-100','99.22','&#160;%','(A-128)*100/128(B-128)*100/128'),
('01','57','2','Short term secondary oxygen sensor trim bank 2 and bank 4','-100','99.22','&#160;%','(A-128)*100/128(B-128)*100/128'),
('01','58','2','Long term secondary oxygen sensor trim bank 2 and bank 4','-100','99.22','&#160;%','(A-128)*100/128(B-128)*100/128'),
('01','59','2','Fuel rail pressure (absolute)','0','655,350','kPa','((A*256)+B) * 10'),
('01','5A','1','Relative accelerator pedal position','0','100','&#160;%','A*100/255'),
('01','5B','1','Hybrid battery pack remaining life','0','100','&#160;%','A*100/255'),
('01','5C','1','Engine oil temperature','-40','210','°C','A - 40'),
('01','5D','2','Fuel injection timing','-210.00','301.992','°','(((A*256)+B)-26,880)/128'),
('01','5E','2','Engine fuel rate','0','3212.75','L/h','((A*256)+B)*0.05'),
('01','5F','1','Emission requirements to which vehicle is designed','','','','Bit Encoded'),
('01','60','4','PIDs supported [61 - 80]','','','','Bit encoded [A7..D0] == [PID $61..PID $80] <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','61','1','Driver\'s demand engine - percent torque','-125','125','&#160;%','A-125'),
('01','62','1','Actual engine - percent torque','-125','125','&#160;%','A-125'),
('01','63','2','Engine reference torque','0','65,535','Nm','A*256+B'),
('01','64','5','Engine percent torque data','-125','125','&#160;%','A-125 IdleB-125 Engine point 1C-125 Engine point 2D-125 Engine point 3E-125 Engine point 4'),
('01','65','2','Auxiliary input / output supported','','','','Bit Encoded'),
('01','66','5','Mass air flow sensor','','','',''),
('01','67','3','Engine coolant temperature','','','',''),
('01','68','7','Intake air temperature sensor','','','',''),
('01','69','7','Commanded EGR and EGR Error','','','',''),
('01','6A','5','Commanded Diesel intake air flow control and relative intake air flow position','','','',''),
('01','6B','5','Exhaust gas recirculation temperature','','','',''),
('01','6C','5','Commanded throttle actuator control and relative throttle position','','','',''),
('01','6D','6','Fuel pressure control system','','','',''),
('01','6E','5','Injection pressure control system','','','',''),
('01','6F','3','Turbocharger compressor inlet pressure','','','',''),
('01','70','9','Boost pressure control','','','',''),
('01','71','5','Variable Geometry turbo (VGT) control','','','',''),
('01','72','5','Wastegate control','','','',''),
('01','73','5','Exhaust pressure','','','',''),
('01','74','5','Turbocharger RPM','','','',''),
('01','75','7','Turbocharger temperature','','','',''),
('01','76','7','Turbocharger temperature','','','',''),
('01','77','5','Charge air cooler temperature (CACT)','','','',''),
('01','78','9','Exhaust Gas temperature (EGT) Bank 1','','','','Special PID. <a href="#Mode_1_PID_78">See below.</a>'),
('01','79','9','Exhaust Gas temperature (EGT) Bank 2','','','','Special PID. <a href="#Mode_1_PID_78">See below.</a>'),
('01','7A','7','Diesel particulate filter (DPF)','','','',''),
('01','7B','7','Diesel particulate filter (DPF)','','','',''),
('01','7C','9','Diesel Particulate filter (DPF) temperature','','','',''),
('01','7D','1','NOx NTE control area status','','','',''),
('01','7E','1','PM NTE control area status','','','',''),
('01','7F','13','Engine run time','','','',''),
('01','80','4','PIDs supported [81 - A0]','','','','Bit encoded [A7..D0] == [PID $81..PID $A0] <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','81','21','Engine run time for Auxiliary Emissions Control Device(AECD)','','','',''),
('01','82','21','Engine run time for Auxiliary Emissions Control Device(AECD)','','','',''),
('01','83','5','NOx sensor','','','',''),
('01','84','','Manifold surface temperature','','','',''),
('01','85','','NOx reagent system','','','',''),
('01','86','','Particulate matter (PM) sensor','','','',''),
('01','87','','Intake manifold absolute pressure','','','',''),
('01','A0','4','PIDs supported [A1 - C0]','','','','Bit encoded [A7..D0] == [PID $A1..PID $C0] <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','C0','4','PIDs supported [C1 - E0]','','','','Bit encoded [A7..D0] == [PID $C1..PID $E0] <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('01','C3','&#160;?','&#160;?','&#160;?','&#160;?','&#160;?','Returns numerous data, including Drive Condition ID and Engine Speed*'),
('01','C4','&#160;?','&#160;?','&#160;?','&#160;?','&#160;?','B5 is Engine Idle RequestB6 is Engine Stop Request*'),
('02','02','2','Freeze frame trouble code','','','','BCD encoded, <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('03','N/A','n*6','Request trouble codes','','','','3 codes per message frame, BCD encoded. <a href="#Bitwise_encoded_PIDs">See below.</a>'),
('04','N/A','0','Clear trouble codes / Malfunction indicator lamp (MIL) / Check engine light','','','','Clears all stored trouble codes and turns the MIL off.'),
('05','0100','','OBD Monitor IDs supported ($01 – $20)','','','',''),
('05','0101','','O2 Sensor Monitor Bank 1 Sensor 1','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0102','','O2 Sensor Monitor Bank 1 Sensor 2','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0103','','O2 Sensor Monitor Bank 1 Sensor 3','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0104','','O2 Sensor Monitor Bank 1 Sensor 4','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0105','','O2 Sensor Monitor Bank 2 Sensor 1','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0106','','O2 Sensor Monitor Bank 2 Sensor 2','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0107','','O2 Sensor Monitor Bank 2 Sensor 3','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0108','','O2 Sensor Monitor Bank 2 Sensor 4','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0109','','O2 Sensor Monitor Bank 3 Sensor 1','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','010A','','O2 Sensor Monitor Bank 3 Sensor 2','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','010B','','O2 Sensor Monitor Bank 3 Sensor 3','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','010C','','O2 Sensor Monitor Bank 3 Sensor 4','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','010D','','O2 Sensor Monitor Bank 4 Sensor 1','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','010E','','O2 Sensor Monitor Bank 4 Sensor 2','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','010F','','O2 Sensor Monitor Bank 4 Sensor 3','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0110','','O2 Sensor Monitor Bank 4 Sensor 4','0.00','1.275','Volts','0.005 Rich to lean sensor threshold voltage'),
('05','0201','','O2 Sensor Monitor Bank 1 Sensor 1','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0202','','O2 Sensor Monitor Bank 1 Sensor 2','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0203','','O2 Sensor Monitor Bank 1 Sensor 3','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0204','','O2 Sensor Monitor Bank 1 Sensor 4','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0205','','O2 Sensor Monitor Bank 2 Sensor 1','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0206','','O2 Sensor Monitor Bank 2 Sensor 2','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0207','','O2 Sensor Monitor Bank 2 Sensor 3','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0208','','O2 Sensor Monitor Bank 2 Sensor 4','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0209','','O2 Sensor Monitor Bank 3 Sensor 1','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','020A','','O2 Sensor Monitor Bank 3 Sensor 2','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','020B','','O2 Sensor Monitor Bank 3 Sensor 3','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','020C','','O2 Sensor Monitor Bank 3 Sensor 4','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','020D','','O2 Sensor Monitor Bank 4 Sensor 1','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','020E','','O2 Sensor Monitor Bank 4 Sensor 2','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','020F','','O2 Sensor Monitor Bank 4 Sensor 3','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('05','0210','','O2 Sensor Monitor Bank 4 Sensor 4','0.00','1.275','Volts','0.005 Lean to Rich sensor threshold voltage'),
('09','00','4','mode 9 supported PIDs 01 to 20','','','','Bit encoded'),
('09','01','1x5','VIN Message Count in command 09 02','','','','Returns 1 line/packet (49 01 05 00 00 00 00), where 05 means 05 packets will be returned in VIN digits.'),
('09','02','5x5','Vehicle identification number (<a href="/wiki/Vehicle_Identification_Number" title="Vehicle Identification Number">VIN</a>)','','','','Returns the VIN as a multi-frame response using the <a href="/wiki/ISO-TP" title="ISO-TP" class="mw-redirect">ISO 15765-2</a> protocol. This is typically five frames, with the first frame encoding the size and count.'),
('09','03','varies','calibration ID message count from mode $09 pid 04','','',''),
('09','04','varies','calibration ID','','','','Returns multiple lines, ASCII coded'),
('09','05','varies','calibration verification numbers message count from mode $09 pid 06','','','','Returns multiple lines, ASCII coded'),
('09','06','4','calibration verification numbers','','','',''),
('09','07','','in-use performance tracking message count from mode $09 pid 08','','','',''),
('09','08','','in-use performance tracking','','','',''),
('09','09','','ECU name message count from mode $09 pid 0a','','','',''),
('09','0a','','ECU name','','','',''),
('09','0b','','in-use performance tracking','','','','',)
]
