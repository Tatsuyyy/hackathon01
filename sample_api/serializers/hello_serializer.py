from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """
    練習用にHello Worldを返すシリアライザ
    """    
    def get_message(self):
        return 'Hello World'
