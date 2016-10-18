#!/usr/bin/env python


def convert_from_strarray(str_array):
    """
    string 配列を文字列に変換
    :param str_array: 文字列が格納された配列
    :return: html用配列文字列
    """
    return u"[\"" + u"\",\"".join(str_array) + u"\"]"


def convert_from_intarray(int_array):
    """
    integer配列を文字列に変換
    :param int_array: integerが格納された配列
    :return: html用配列文字列
    """
    str_array = map(str, int_array)
    return u"[" + u",".join(str_array) + u"]"

