#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from rest_framework                     import serializers
from rest_framework.authtoken.models    import Token

from restAPICore.serializers            import ModelSerializer

from userAccount.models                 import UserAccount


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
#
## @brief [ REST FRAMEWORK MODEL SERIALIZER CLASS ] - Model serializer class.
class TokenSerializer(serializers.ModelSerializer):

    #
    ## @brief [ REST FRAMEWORK SERIALIZER META CLASS ] - Overwritten meta class.
    class Meta:

        ## [ django.db.models.Model ] - Django Model Class object.
        model   = Token

        ## [ tuple ] - Exclude fields.
        exclude = ('created',)

#
## @brief [ REST FRAMEWORK MODEL SERIALIZER CLASS ] - Model serializer class.
class UserAccountSuperUserSerializer(ModelSerializer):

    ## [ userAccount.serializers.TokenSerializer ] - Serializer.
    api_token       = TokenSerializer(many=False, read_only=True)

    ## [ rest_framework.serializers.EmailField ] - Serializer.
    email           = serializers.EmailField(required=False)

    #
    ## @brief [ REST FRAMEWORK SERIALIZER META CLASS ] - Overwritten meta class.
    class Meta:

        ## [ django.db.models.Model ] - Django Model Class object.
        model               = UserAccount

        ## [ dict ] - Extra keyword arguments.
        extra_kwargs        = {'password':{'write_only':True, 'required':False}}

        ## [ tuple ] - Exclude fields.
        exclude             = ('account_verification_id',
                               'groups',
                               'user_permissions',)

        ## [ tuple ] - Read only fields.
        read_only_fields    = ('folder_name',
                               'last_login',
                               'registration_date_time')

    #
    ## @brief Validate data.
    #
    #  @param data [ dict | None | in  ] - Data.
    #
    #  @exception serializers.ValidationError - If data validation fails.
    #
    #  @return dict - Data.
    def validate(self, data):

        if self.context['request'].method == 'POST':

            if not 'email' in data:
                raise serializers.ValidationError({'email':['email field must be provided']})

            if not 'password' in data:
                raise serializers.ValidationError({'password':['password field must be provided']})

            if self.Meta.model.objects.filter(email=data['email']):
                raise serializers.ValidationError({'email':['This email already taken']})

        return data

    #
    ## @brief Create object.
    #
    #  @param validated_data [ dict | None | in  ] - Validated data.
    #
    #  @exception N/A
    #
    #  @return userAccount.models.UserAccount - Model class instance.
    def create(self, validated_data):

        password = validated_data.pop('password')

        userAccount = UserAccount(**validated_data)
        userAccount.set_password(password)
        userAccount.save()

        return userAccount

    #
    ## @brief Update object.
    #
    #  @exception N/A
    #
    #  @return userAccount.models.UserAccount - Model class instance.
    def update(self, instance, validated_data):

        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance

#
## @brief [ REST FRAMEWORK MODEL SERIALIZER CLASS ] - Model serializer class.
class UserAccountSerializer(ModelSerializer):

    ## [ userAccount.serializers.TokenSerializer ] - Serializer.
    api_token       = TokenSerializer(many=False, read_only=True)

    ## [ rest_framework.serializers.EmailField ] - Serializer.
    email           = serializers.EmailField(required=False)

    #
    ## @brief [ REST FRAMEWORK SERIALIZER META CLASS ] - Overwritten meta class.
    class Meta:

        ## [ django.db.models.Model ] - Django Model Class object.
        model               = UserAccount

        ## [ dict ] - Extra keyword arguments.
        extra_kwargs        = {'password':{'write_only':True, 'required':False}}

        ## [ tuple ] - Exclude fields.
        exclude             = ('is_superuser',
                               'is_staff',
                               'is_active',
                               'account_verification_id',
                               'groups',
                               'user_permissions',)

        ## [ tuple ] - Read only fields.
        read_only_fields    = ('folder_name',
                               'last_login',
                               'registration_date_time',
                               'has_account_been_verified',)

    #
    ## @brief Update object.
    #
    #  @exception N/A
    #
    #  @return userAccount.models.UserAccount - Model class instance.
    def update(self, instance, validated_data):

        if 'password' in validated_data:
            instance.set_password(validated_data.pop('password'))

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance