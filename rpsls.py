#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�Ѧ��
���ڣ�11��19��
"""

import random





# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��
def name_to_number (name):#����Ϸ�����Ӧ����Ӧ������
 if name==str("ʯͷ"):
    number=int(0)
    return number
 elif name==str("ʷ����"):
    number=int(1)
    return number
 elif name==("ֽ"):
    number=int(2)
    return  number
 elif name==("����"):
    number=int(3)
    return number
 elif name==("����"):
    number=int(4)
    return number
 else:print("Error: No Correct Name")








def number_to_name(number):#�����ֶ�Ӧ����Ӧ��Ϸ����
 if number==0:
     name=str("ʯͷ")
     return name
 elif number==1:
     name=str("ʷ����")
     return name
 elif number==2:
     name=str("ֽ")
     return name
 elif number==3:
     name=str("����")
     return name
 elif number==4:
     name=str("����")
     return name


    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��




def rpsls(player_choice):#�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    print("--------")
    player_choice_number=name_to_number(player_choice)
    print("����ѡ��Ϊ��%s"%(player_choice))
    comp_number=random.randint(0,5)#����0-4֮��������������Ϊ��������ѡ�����Ϸ����
    comp_name=number_to_name(comp_number)
    print("�������ѡ��Ϊ��%s"%(comp_name))
    if player_choice_number==0 and comp_number==3:
        print("��Ӯ��!")
    elif player_choice_number==0 and comp_number==4:
        print("��Ӯ��!")
    elif player_choice_number==1 and comp_number==0:
        print("��Ӯ��!")
    elif player_choice_number==1 and comp_number==4:
        print("��Ӯ��!")
    elif player_choice_number==2 and comp_number==0:
        print("��Ӯ��!")
    elif player_choice_number==2 and comp_number==1:
        print("��Ӯ��!")
    elif player_choice_number==3 and comp_number==1:
        print("��Ӯ��!")
    elif player_choice_number==3 and comp_number==2:
        print("��Ӯ��!")
    elif player_choice_number==4 and comp_number==2:
        print("��Ӯ��!")
    elif player_choice_number==4 and comp_number==3:
        print("��Ӯ��!")
    elif player_choice_number==comp_number:
        print("���ͼ��������һ����")
    else:print("�����Ӯ��")


    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """


    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=str(input())
c=rpsls(choice_name)



