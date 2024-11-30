import React from 'react';
import ContentLoader from 'react-content-loader';

export const SkeletonLoader: React.FC = () => (
  <ContentLoader
    speed={2}
    width="100%"
    height={92}
    backgroundColor="#a9a9a9"
    foregroundColor="#858585"
    style={{ borderRadius: '10px' }}>
    <rect x="0" y="0" width="100%" height="100" />
  </ContentLoader>
);
