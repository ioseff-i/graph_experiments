from typing import Any, Dict
class Node:
    def __init__(self,id: Any, label:str, features: Dict[str,Any] = None):
        self.id = id
        self.label = label
        self.features = features if features is not None else {}
        
        
    def __str__(self):
        return f"Node(id={self.id}, label={self.label}, features={self.features})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, value):
        if not isinstance(value, Node):
            return False
        return self.id == value.id
    
    def __hash__(self):
        return hash(self.id)
    
    def get_feature(self, key: str) -> Any:
        return self.features.get(key)
    
    def set_feature(self, key: str, value: Any) -> None:
        self.features[key] = value
        
    def remove_feature(self, key: str) -> None:
        if key in self.features:
            del self.features[key]