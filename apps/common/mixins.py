from django.contrib import messages


class LimitInstancesMixin:
    max_instances = 1
    instance_name = 'object'

    def save_model(self, request, obj, form, change):
        existing_count = self.model.objects.count()

        if existing_count >= self.max_instances:
            if obj.pk:
                super().save_model(request, obj, form, change)
            else:
                message = f"Можно создать только {self.max_instances} {self.instance_name}"
                self.message_user(request, message, level=messages.ERROR)
        else:
            super().save_model(request, obj, form, change)
