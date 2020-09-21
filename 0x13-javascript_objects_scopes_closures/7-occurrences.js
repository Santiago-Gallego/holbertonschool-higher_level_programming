#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(ele => ele === searchElement).length);
};
