import axios from 'axios';

export const axiosInstanсe = axios.create({
  baseURL: 'https://fvbit.ru/api/',
});
