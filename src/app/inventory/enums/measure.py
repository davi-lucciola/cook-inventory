from enum import Enum


class Measure(str, Enum):
    G = 'GRAMA'
    L = 'LITRO'
    ML = 'MILI_LITRO'
    KG = 'KILO_GRAMA'
    UNIT = 'UNIDADE'

    @staticmethod
    def get_values():
        return {
            'G': {
                'label': 'Gramas (g)',
                'acronym': 'g'
            },
            'L': {
                'label': 'Litros (L)',
                'acronym': 'L'
            },
            'ML': {
                'label': 'Mililitros (ml)',
                'acronym': 'ml'
            },
            'KG': {
                'label': 'Kilograma (kg)',
                'acronym': 'kg'
            },
            'UNIT': {
                'label': 'Unidade (uni.)',
                'acronym': 'uni.'
            },
        }