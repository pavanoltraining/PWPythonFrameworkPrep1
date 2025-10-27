from utilities.random_data_util import RandomDataUtil

# Create an instance of the utility
data_util = RandomDataUtil()

print(data_util.get_first_name())
print(data_util.get_email())
print(data_util.get_random_country())
print(data_util.get_random_numeric(6))
print(data_util.get_random_uuid())