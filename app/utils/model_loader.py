import pickle
import os
from pathlib import Path

def load_model(model_path: str = "./model.pkl"):
    """
    Load a pickled model from the specified path.
    
    Args:
        model_path (str): Path to the .pkl file
        
    Returns:
        The unpickled model object
    
    Raises:
        FileNotFoundError: If the model file doesn't exist
        Exception: If there's an error loading the model
    """
    try:
        model_path = Path(model_path)
        if not model_path.exists():
            raise FileNotFoundError(f"Model file not found at {model_path}")
            
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
            return model
            
    except Exception as e:
        raise Exception(f"Error loading model: {str(e)}")

# Example usage:
if __name__ == "__main__":
    try:
        # Load the model
        model = load_model()
        
        # Print model information (type and basic details)
        print(f"Model loaded successfully!")
        print(f"Model type: {type(model)}")
        
        # Example of how to use the model (uncomment and modify based on your model type)
        # For example, if it's a scikit-learn model:
        # prediction = model.predict([[your_input_features]])
        # print(f"Prediction: {prediction}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
