from modeltranslation.translator import translator, TranslationOptions
from .models import Direction


class DirectionTranslationOptions(TranslationOptions):
    fields = ('title', 'text')

translator.register(Direction, DirectionTranslationOptions)