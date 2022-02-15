from rest_framework import serializers

from notifier.models import DirectEmployeeNotifier, DirectEmployerNotifier,HotEmployeeAlert


class EmployeeNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectEmployeeNotifier
        fields = ['id', 'title', 'message', 'is_read', 'created']


class EmployerNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectEmployerNotifier
        fields = ['id', 'title', 'message', 'is_read', 'created']
class HotEmployeeAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotEmployeeAlert
        fields = ['message', 'link']