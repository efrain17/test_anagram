"""This module test algorit controller"""
import pytest 
import algorit


def test_fun_with_anagrams(mocker):
    response = algorit.fun_with_anagrams(['code', 'aaagmnrs', 'anagrams', 'doce'])
    assert response == ['code', 'aaagmnrs']


def test_fun_with_anagrams(mocker):
    text = [
        'spwvpfyfpkvgthqqrmajxispjncxgviyuqavayvsvznmhskodmidajwlkf',
        'imprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqrypstsxhp',
        'rrmbeddvphnegtuxxtalsyxezjwtlwmxvrjtxytykkckuvbhhlovgcxjxhhivxnutkxvhadiaysulvknmcanhsyxlivarjdk',
        'fcfpotnvlcibpxkidmwexpugwoxjicdkvstltienwqngiutnuqbzicontzlybgvumnwehj',
        'oswnprlhvsuzvgyeettenngipfvrflpprjjalchhhcmhxkupciulccqssaqgdttpldmzdzveslyjadswtsbhgkddeouxbldsxzmfvhtonlampljgzyvem',
        'hnlcrldtfthulkxhflcoupgeikrlaksuyfqvnvtnqs',
        'imprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqryptpsxsh',
        'fcfpotnvlcibpxkidmwexpugwoxjicdkvstltienwqngiutnuqbzicontzlybgvunhjewm',
        'imprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqrypsxpsth',
        'imprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqrypsxthsp',
        'fcfpotnvlcibpxkidmwexpugwoxjicdkvstltienwqngiutnuqbzicontzlybgvunjhmew'
    ]
    expected = [
        'fcfpotnvlcibpxkidmwexpugwoxjicdkvstltienwqngiutnuqbzicontzlybgvumnwehj',
        'hnlcrldtfthulkxhflcoupgeikrlaksuyfqvnvtnqs',
        'imprrhenguipdghstyopbvuiqcoplvwduwmjpblqoafnxwgqtvwztjekxwnbcuggliiehimvoymyjasinwspsqiukflhyfacamqrbqrypstsxhp',
        'oswnprlhvsuzvgyeettenngipfvrflpprjjalchhhcmhxkupciulccqssaqgdttpldmzdzveslyjadswtsbhgkddeouxbldsxzmfvhtonlampljgzyvem',
        'rrmbeddvphnegtuxxtalsyxezjwtlwmxvrjtxytykkckuvbhhlovgcxjxhhivxnutkxvhadiaysulvknmcanhsyxlivarjdk',
        'spwvpfyfpkvgthqqrmajxispjncxgviyuqavayvsvznmhskodmidajwlkf'
    ]
    response = algorit.fun_with_anagrams(text)
    assert response == expected
