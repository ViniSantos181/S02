from database import Database
from motoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

db = Database(database="avaliativo01-lab", collection="Motoristas")

motoristaDAO = MotoristaDAO(database=db)
motoristaCLI = MotoristaCLI(motoristaDAO)
motoristaCLI.run()