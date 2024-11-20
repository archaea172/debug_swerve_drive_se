import serial
import serial.tools.list_ports
import cv2
import numpy as np
import math

Serial_Port=serial.Serial(port='COM15', baudrate=115200, parity= 'N')
while(1):
    data=Serial_Port.readline() # 1byte受信なら data=Serial_Port.read(1)
    data=data.strip()
    data=data.decode('utf-8')
    data_list = data.split(",")
    int_data_list = []
    for i in range(len(data_list)):
        int_data_list.append(float(data_list[i]))
    print(int_data_list)

    img = np.full((500, 500, 3), 128, dtype=np.uint8)
    x1 = 50*math.cos(int_data_list[0])
    y1 = 50*math.sin(int_data_list[0])
    x2 = 50*math.cos(int_data_list[1])
    y2 = 50*math.sin(int_data_list[1])
    x3 = 50*math.cos(int_data_list[2])
    y3 = 50*math.sin(int_data_list[2])
    start_point1 = (int(250 - x1 + 50*math.sqrt(3)), int(250 + y1 - 50))
    end_point1   = (int(250 + x1 + 50*math.sqrt(3)), int(250 - y1 - 50))
    start_point2 = (int(250 - x2 - 50*math.sqrt(3)), int(250 + y2 - 50))
    end_point2   = (int(250 + x2 - 50*math.sqrt(3)), int(250 - y2 - 50))
    start_point3 = (int(250 - x3),                   int(250 + y3 + 100))
    end_point3   = (int(250 + x3),                   int(250 - y3 + 100))
    
    cv2.line(img, start_point1, end_point1, (255, 0, 0), thickness=4, lineType=cv2.LINE_AA)
    cv2.line(img, start_point2, end_point2, (255, 0, 0), thickness=4, lineType=cv2.LINE_AA)
    cv2.line(img, start_point3, end_point3, (255, 0, 0), thickness=4, lineType=cv2.LINE_AA)
    
    x12 = 50*math.cos(int_data_list[3])
    y12 = 50*math.sin(int_data_list[3])
    x22 = 50*math.cos(int_data_list[4])
    y22 = 50*math.sin(int_data_list[4])
    x32 = 50*math.cos(int_data_list[5])
    y32 = 50*math.sin(int_data_list[5])
    start_point12 = (int(250 - x12 + 50*math.sqrt(3)), int(250 + y12 - 50))
    end_point12   = (int(250 + x12 + 50*math.sqrt(3)), int(250 - y12 - 50))
    start_point22 = (int(250 - x22 - 50*math.sqrt(3)), int(250 + y22 - 50))
    end_point22   = (int(250 + x22 - 50*math.sqrt(3)), int(250 - y22 - 50))
    start_point32 = (int(250 - x32),                   int(250 + y32 + 100))
    end_point32   = (int(250 + x32),                   int(250 - y32 + 100))

    cv2.line(img, start_point12, end_point12, (0, 255, 0), thickness=4, lineType=cv2.LINE_AA)
    cv2.line(img, start_point22, end_point22, (0, 255, 0), thickness=4, lineType=cv2.LINE_AA)
    cv2.line(img, start_point32, end_point32, (0, 255, 0), thickness=4, lineType=cv2.LINE_AA)
    #cv2.imshow("img2", img2)
    cv2.imshow("img", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

