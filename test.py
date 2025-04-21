import subprocess
import os
from pathlib import Path
import json
import math
import time
import shutil
from pg_database import Database
from TPCH import TPCH



# Run it directly
if __name__ == "__main__":
    db = Database()
    db.analyze_tables()
