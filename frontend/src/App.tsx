import { Navigate, Route, Routes } from 'react-router-dom';
import { ChatMembers } from './pages';
import { Chat } from './pages/сhat';
import './sass/app.scss';

export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/chats" />} />
      <Route path="/chats" element={<Chat />} />
      <Route path="/chats-member/:id" element={<ChatMembers />} />
    </Routes>
  );
};
