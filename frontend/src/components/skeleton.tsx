import React from 'react';
import ContentLoader from 'react-content-loader';

export const SkeletonLoader: React.FC = () => (
  <ContentLoader
    speed={2}
    width="100%"
    height={92}
    backgroundColor="#111d3a"
    foregroundColor="#040d21"
    style={{ borderRadius: '10px' }}>
    <rect x="0" y="0" width="100%" height="100" />
  </ContentLoader>
);
