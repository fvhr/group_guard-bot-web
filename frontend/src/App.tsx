import { Navigate, Route, Routes } from 'react-router-dom';
import { ChatMembers, LoginSms, LoginTelegramm } from './pages';
import { LoginPhone } from './pages/login-phone';
import { Chat } from './pages/сhat';
import './sass/app.scss';

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<LoginTelegramm />} />
      <Route path="/login-phone" element={<LoginPhone />} />
      <Route path="/login-sms" element={<LoginSms />} />
      <Route path="/chats" element={<Chat />} />
      <Route path="/chats-member/:id" element={<ChatMembers />} />
    </Routes>
  );
};
