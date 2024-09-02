import threading
import time
import random
from pymongo import MongoClient

# -*- coding: utf-8 -*-

# Conecta ao MongoDB
client = MongoClient('mongodb+srv://root:root@cluster0.girhc.mongodb.net/')
db = client['bancoiot']
collection = db['sensors']

# Função que simula a leitura de temperatura de um sensor
def sensor_simulation(sensor_name, interval):
    while True:
        # Gera uma temperatura aleatória entre 30 e 40 °C
        temp_value = round(random.uniform(30, 40), 2)
        
        # Exibe a temperatura gerada
        print(f"Sensor {sensor_name} - Temperatura: {temp_value}C")
        
        # Verifica se o sensor deve ser alarmado
        sensor_alarm = temp_value > 38
        
        # Cria ou atualiza documento para o sensor
        sensor_data = {
            'nomeSensor': sensor_name,
            'valorSensor': temp_value,
            'unidadeMedida': 'C', 
            'sensorAlarmado': sensor_alarm
        }
        
        try:
            # Insere ou atualiza os dados no MongoDB
            collection.update_one(
                {'nomeSensor': sensor_name},
                {'$set': sensor_data},
                upsert=True
            )
        except Exception as e:
            print(f"Erro ao atualizar o banco de dados: {e}")
        
        # Exibe o alerta no terminal se a temperatura for muito alta
        if sensor_alarm:
            print(f"Atencao! Temperatura muito alta! Verificar Sensor {sensor_name}!")
        
        # Aguarda o próximo ciclo de leitura
        time.sleep(interval)

# Cria e inicia 3 threads para simular 3 sensores
sensors = ['Temp1', 'Temp2', 'Temp3']
threads = []

for sensor in sensors:
    t = threading.Thread(target=sensor_simulation, args=(sensor, 5))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
