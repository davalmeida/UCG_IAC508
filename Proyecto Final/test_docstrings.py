
import pytest
from pipeline import DataPipeline

def test_docstrings_presence():
    """Test para verificar que todos los métodos de DataPipeline tienen docstrings"""
    pipeline = DataPipeline()
    
    # Verificar que la clase tiene docstring
    assert DataPipeline.__doc__ is not None
    assert len(DataPipeline.__doc__.strip()) > 0
    
    # Verificar que todos los métodos tienen docstrings
    methods = ['__init__', 'preprocess', 'train', 'evaluate']
    
    for method_name in methods:
        method = getattr(pipeline, method_name)
        assert method.__doc__ is not None, f"El método {method_name} no tiene docstring"
        assert len(method.__doc__.strip()) > 0, f"El método {method_name} tiene docstring vacío"
        
        # Verificar que el docstring contiene información útil
        doc = method.__doc__.lower()
        
        # Para métodos que no son __init__, verificar que documentan parámetros y retorno
        if method_name != '__init__':
            assert 'args' in doc or 'parámetros' in doc or 'param' in doc, f"El método {method_name} no documenta sus parámetros"
            assert 'return' in doc or 'devuelve' in doc, f"El método {method_name} no documenta su valor de retorno"
        else:
            # Para __init__, solo verificar que tiene documentación
            assert len(doc) > 50, f"El método {method_name} tiene documentación insuficiente"