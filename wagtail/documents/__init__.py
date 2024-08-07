from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def get_document_model_string():
    """
    Get the dotted ``app.Model`` name for the document model as a string.
    Useful for developers making Wagtail plugins that need to refer to the
    document model, such as in foreign keys, but the model itself is not required.
    """
    return getattr(settings, "WAGTAILDOCS_DOCUMENT_MODEL", "wagtaildocs.Document")


def get_document_model():
    """
    Get the document model from the ``WAGTAILDOCS_DOCUMENT_MODEL`` setting.
    Defaults to the standard ``wagtail.documents.models.Document`` model
    if no custom model is defined.
    """
    from django.apps import apps

    model_string = get_document_model_string()
    try:
        return apps.get_model(model_string, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured(
            "WAGTAILDOCS_DOCUMENT_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            "WAGTAILDOCS_DOCUMENT_MODEL refers to model '%s' that has not been installed"
            % model_string
        )
