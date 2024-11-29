import { Navigate, Route, Routes } from 'react-router-dom';
import { Login } from './pages/Login';
import './sass/app.scss';

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  );
};
