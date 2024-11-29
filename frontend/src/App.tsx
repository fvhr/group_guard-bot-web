import { Navigate, Route, Routes } from 'react-router-dom';
import { ChatMembers, LoginSms } from './pages';
import { Chat } from './pages/Chat';
import { LoginPhone } from './pages/LoginPhone';
import './sass/app.scss';

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login-phone" />} />
      <Route path="/login-phone" element={<LoginPhone />} />
      <Route path="/login-sms" element={<LoginSms />} />
      <Route path="/chats" element={<Chat />} />
      <Route path="/chats-members" element={<ChatMembers />} />
    </Routes>
  );
};
