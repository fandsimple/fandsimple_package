class User:
    def __init__(self, id, bmi):
        self.id = id
        self.bmi = bmi

    def __str__(self):
        return '{}:{}'.format(self.id, self.bmi)

    __repr__ = __str__


class UserManager:
    BMI_FAT_RANGE = [24.0, 27.9]

    def __init__(self, user_list):
        self.user_list = user_list

    @property
    def users(self):
        return self.user_list

    def is_fat_user(self, user):
        return self.BMI_FAT_RANGE[0] <= user.bmi <= self.BMI_FAT_RANGE[1]

    def remove_fat_user(self):
        delUserList = [] # 添加
        for user in self.user_list:
            if self.is_fat_user(user):
                # self.user_list.remove(user) # 当前self.user_list正在被迭代，删除数据会影响迭代操作
                delUserList.append(user)

        for item in delUserList: # 添加
            self.user_list.remove(item) # 添加


    def get_user_list_bmi_differ_is(self, differ):
        self.user_list = sorted(user_list, key=lambda user: user.bmi)
        result = []

        for i in range(1, len(self.user_list)):
            prev_user = self.user_list[i - 1]
            curr_user = self.user_list[i]
            if round(abs(curr_user.bmi - prev_user.bmi), 1) == differ: # 浮点数相减问题
                result.append((prev_user, curr_user))
        return result

    @staticmethod
    def generate_user_data():
        bmi_list = [18.5, 26.5, 18.5, 20.2, 20.3, 24.8, 20.9, 21.3, 21.8, 25.2]
        user_list = []
        for id, bmi in enumerate(bmi_list, 1):
            user_list.append(User(id, bmi))
        return user_list


if __name__ == '__main__':
    user_list = UserManager.generate_user_data()
    user_manager = UserManager(user_list)
    user_list = user_manager.users
    print('原始数据：')
    print(user_list)
    print('========')
    # 找出 BMI 相差 0.1 的用户
    # 正确的输出结果 [4:20.2, 5:20.3]
    print('BMI 相差 0.1 的用户：')
    print(user_manager.get_user_list_bmi_differ_is(0.1))
    print('========')
    # 移除肥胖的用户
    # 肥胖的用户 [2:26.5, 6:24.8, 10:25.2]
    # 正确的输出结果 [1:18.5, 3:18.5, 4:20.2, 5:20.3, 7:20.9, 8:21.3, 9:21.8]
    print('健康的用户：')
    user_manager.remove_fat_user()
    print(user_manager.users)
