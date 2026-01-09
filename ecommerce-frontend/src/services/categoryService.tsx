// src/services/categoryService.tsx
import { Category } from '../types/Category';
import { api } from './api';

export const categoryService = {
    getAllCategories: async (): Promise<Category[]> => {
        const response = await api.get<Category[]>('/categories');
        return response.data;
    },

    getCategory: async (id: number): Promise<Category> => {
        const response = await api.get<Category>(`/categories/${id}`);
        return response.data;
    },

    createCategory: async (categoryData: Partial<Category>): Promise<Category> => {
        const response = await api.post<Category>('/categories', categoryData);
        return response.data;
    },
    
    updateCategory: async (id: number, categoryData: Partial<Category>): Promise<Category> => {
        const response = await api.put<Category>(`/categories/${id}`, categoryData);
        return response.data;
    },

    deleteCategory: async (id: number): Promise<void> => {
        await api.delete(`/categories/${id}`);
    },
}