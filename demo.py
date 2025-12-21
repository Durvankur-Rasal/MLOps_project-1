
from src.pipline.training_pipeline import TrainPipeline
from dotenv import load_dotenv
load_dotenv()

pipeline = TrainPipeline()
pipeline.run_pipeline()