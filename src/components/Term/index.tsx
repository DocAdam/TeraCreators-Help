import React from 'react';
import {hh3Terms, type HH3TermName} from '@site/src/data/hh3Terms';

type TermProps = {
  name: HH3TermName;
  children?: React.ReactNode;
};

export default function Term({name, children}: TermProps) {
  const definition = hh3Terms[name];

  return (
    <span
      title={definition}
      style={{
        textDecoration: 'underline dotted',
        cursor: 'help',
      }}
      aria-label={`${name}: ${definition}`}
    >
      {children ?? name}
    </span>
  );
}
