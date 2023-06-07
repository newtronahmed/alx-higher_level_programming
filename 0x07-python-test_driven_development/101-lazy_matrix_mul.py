#!/usr/bin/python3
"""This module contains the numpy matrix mul implementation"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Given two matrix, it multiplies the two.
    Args:
        m_a(matrix): matrix a.
        m_b(matrix): matrix b.
    Result:
        m_a * m_b
    """

    return numpy.matmul(m_a, m_b)
