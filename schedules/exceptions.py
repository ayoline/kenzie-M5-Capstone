from rest_framework.exceptions import APIException
from rest_framework.views import status


class MedicoPacienteCategoriasDiferentesError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'O médico e o paciente devem pertencer a mesma categoria.'


class ConsultaEtapa1Error(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Na etapa 1 o médico deve obrigatóriamente ser um Clínico Geral.'


class ConsultaEtapa2Error(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Na etapa 2 o médico não deve ser um Clínico Geral, deve ser um especialista.'


class MedicoErradoError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Médico incompátivel com a especialidade requerida.'