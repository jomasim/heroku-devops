import re


class Request():

    def __init__(self, request, schema):
        self.request = request
        self.schema = schema

    ''' this method validates all fields in a request '''

    def validate(self):
        ''' all request rules '''
        all_rules = self.get_request_rules()
        all_errors = {}
        ''' get all errors from request  '''
        for field_rules in all_rules:
            ''' get all errors for a single field '''
            field_error = self.validate_field(
                field_rules, all_rules[field_rules])
            if field_error:
                all_errors[field_rules] = field_error

        if all_errors:
                return {"errors": all_errors}
        return None

    ''' this method gets all field rules from filed rules string '''
    @staticmethod
    def get_field_rules(rules_string):
        return rules_string.split('|')

    ''' gets all request validation rules for each field '''

    def get_request_rules(self):
        fields = self.schema
        request_rules = {}
        for field in fields:
            request_rules[field] = Request.get_field_rules(fields[field])
        return request_rules

    def isEmpty(self, arg):
        if arg == "":
            return True
        return False

    @staticmethod
    def isEmail(arg):
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", str(arg)):
            return True
        return False

    @staticmethod
    def isMin(arg, field_rules):
        min_length = Request.get_rule_argument("min", field_rules)
        if len(str(arg)) < int(min_length):
            return True
        return False

    @staticmethod
    def isMax(arg, field_rules):
        max_length = Request.get_rule_argument("max", field_rules)
        if len(str(arg)) > int(max_length):
            return True
        return False

    def validate_field(self, field, field_rules):
        value = self.get_value(field)
        field_errors = []

        if 'required' in field_rules and value == None or self.isEmpty(value):
            field_errors.append(field + " is required")
        ''' if required field is empty or null return'''
        if field_errors:
            return field_errors

        ''' collect all other errors '''

        length_errors=Request.is_allowed_length(field,value,field_rules)
        instance_errors=Request.is_type_instance(field,value,field_rules)
        type_errors=Request.is_type(value,field_rules)

        ''' include collected errors to field errors '''
        field_errors=field_errors+instance_errors+type_errors+length_errors

        return field_errors

    def get_value(self, field_key):
        ''' get field value from request using key '''
        if field_key in self.request:
            return self.request[field_key]
        return None

    @staticmethod
    def get_rule_argument(type, field_rules):
        pieces = []
        for rule in field_rules:
            if rule.startswith(type):
                pieces = rule.split(':')
                return pieces[1]
        return None

    @staticmethod
    def is_type_instance(field, value, field_rules):
        ''' method returns all instance errors '''
        field_errors = []
        if 'string' in field_rules and not isinstance(value, str):
            field_errors.append(field + " should be a string")

        if 'int' in field_rules and not isinstance(value, int):
            field_errors.append(field + " should be an integer")
        return field_errors

    @staticmethod
    def is_allowed_length(field, value, field_rules):
        ''' method returns all field length errors '''
        field_errors = []
        min_length = Request.get_rule_argument("min", field_rules)
        max_length = Request.get_rule_argument("max", field_rules)

        if min_length and Request.isMin(value,field_rules):
            field_errors.append(field + " should have a minimum of " + min_length + " characters")
        if max_length and Request.isMax(value,field_rules):
            field_errors.append(field + " should have a maximum of "+ max_length + " characters")
        return field_errors

    @staticmethod
    def is_type(value,field_rules):
        ''' return type errors i.e password,email '''
        field_errors=[]
        if 'email' in field_rules and not Request.isEmail(value):
            field_errors.append(value + " not a valid email")
        return field_errors

