#
# ----------------------------------------------------------------------------------------------------
# DESCRIPTION
# ----------------------------------------------------------------------------------------------------


#
# ----------------------------------------------------------------------------------------------------
# IMPORTS
# ----------------------------------------------------------------------------------------------------
from django.test    import TestCase

from userAccount    import models


#
# ----------------------------------------------------------------------------------------------------
# CODE
# ----------------------------------------------------------------------------------------------------
USER_ACCOUNTS = [
                {
                    'is_superuser'              : False,
                    'is_staff'                  : False,
                    'is_active'                 : True,
                    'email'                     : 'a.dumas@cristo.com',
                    'first_name'                : 'Alexandre',
                    'last_name'                 : 'Dumas',
                    'password'                  : '123',
                    'avatar'                    : None,
                    'has_account_been_verified' : True
                },
                {
                    'is_superuser'              : False,
                    'is_staff'                  : False,
                    'is_active'                 : True,
                    'email'                     : 'jverne@thousandleagues.com',
                    'first_name'                : 'Jules',
                    'last_name'                 : 'Verne',
                    'password'                  : '123',
                    'avatar'                    : None,
                    'has_account_been_verified' : True
                }
            ]

class UserAccountTest(TestCase):

    def setUp(self):

        for data in USER_ACCOUNTS:

            modelInstance = models.UserAccount.objects.create(**data)
            modelInstance.set_password(data['password'])
            modelInstance.save()

    def test_userAccount(self):

        modelInstance = models.UserAccount.objects.get(email=USER_ACCOUNTS[0]['email'])

        self.assertEqual(modelInstance.is_superuser             , USER_ACCOUNTS[0]['is_superuser'])
        self.assertEqual(modelInstance.is_staff                 , USER_ACCOUNTS[0]['is_staff'])
        self.assertEqual(modelInstance.is_active                , USER_ACCOUNTS[0]['is_active'])

        self.assertEqual(modelInstance.first_name               , USER_ACCOUNTS[0]['first_name'])
        self.assertEqual(modelInstance.last_name                , USER_ACCOUNTS[0]['last_name'])
        self.assertEqual(modelInstance.avatar                   , '')
        self.assertEqual(modelInstance.has_account_been_verified, USER_ACCOUNTS[0]['has_account_been_verified'])

        self.assertTrue(modelInstance.check_password(USER_ACCOUNTS[0]['password']), True)



