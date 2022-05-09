"""Code based on UML diagram."""


class Customer:
    """Customer class."""

    def __init__(self):
        """Customer constructor."""
        self.name = None
        self.address = None
        self.dob = None
        self.card_number = None
        self.pin = None

    def verify_password(self, password):
        """Verify password."""
        pass


class ATM:
    """ATM class."""

    def __init__(self):
        """ATM constructor."""
        self.location = None
        self.managed_by = None

    def identifies(self, customer):
        """Identifies."""
        pass

    def transactions(self):
        """Transactions."""
        pass


class Account:
    """Account class."""

    def __init__(self):
        """Account constructor."""
        self.number = None
        self.__balance = None

    def _authenticate(self, pin):
        """Authenticate."""
        pass

    def deposit(self, amount):
        """Deposit."""
        pass

    def withdraw(self, amount):
        """Withdraw."""
        pass

    def __create_transaction(self, datetime):
        """Create transaction."""
        pass


class Bank:
    """Bank class."""

    def __init__(self, code, address):
        """Bank constructor."""
        self.code = code
        self.address = address
        self.__revenue = None

    def __manages(self):
        """Manages."""
        pass

    def __maintains(self):
        """Maintains."""
        pass

    def _print_revenue(self, sender, receiver):
        """Print revenue."""
        pass


class ATMTransactions:
    """ATM Transactions class."""

    def __init__(self):
        """ATM Transactions constructor."""
        self.transaction_id = None
        self.date = None
        self.type = None
        self.amount = None
        self.post_balance = None

    def updates(self, account):
        """Updates."""
        pass


class CurrentAccount:
    """Current Account class."""

    def __init__(self):
        """Current Account constructor."""
        self.account_no = None
        self.balance = None
        self.interest_rate = None

    def withdraw(self, amount):
        """Withdraw."""
        pass

    def apply_interest(self):
        """Apply interest."""
        pass


class SavingAccount:
    """Saving Account class."""

    def __init__(self, num, holder: Account, credit_range):
        """Saving Account constructor."""
        self.balance = num
        self.account_no = holder.number
        self.__credit_range = credit_range

    def withdraw(self, amount):
        """Withdraw."""
        pass
