# -*- coding: utf-8 -*-

# Copyright 2011 Tom SF Haines

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.



import numpy



class Topic:
  """Simple wrapper class for a topic - contains just the parameter vector for the multinomial distribution from which words in that topic are drawn from. The index into the vector is the ident of the word associated with each specific probability value."""
  def __init__(self, ident):
    """Initialises the model to be None, so it can be later calculated. ident is the offset of this topic into the Corpus in which this topic is stored. Only Corpus-s should initialise this object and hence should know."""
    self.model = None
    self.mult = None # Multiplier of model to get P(word|topic)
    self.ident = ident


  def getIdent(self):
    """Ident - just the offset into the array in the Corpus where this topic is stored."""
    return self.ident


  def getModel(self):
    """Returns the unnormalised parameter vector for the multinomial distribution from which words generated by the topic are drawn. (The probabilities are actually a list of P(topic,word) for this topic, noting that there are all the other topics. You may normalise it to get P(word|topic), or take the other vectors and manipulate them to get all the relevant distributions, i.e. P(topic|word), P(topic), P(word). )"""
    return self.model

  def getNormModel(self):
    """Returns the model but normalised so it is the multinomial P(word|topic)."""
    return self.model * self.mult
  
  def setModel(self,model):
    self.model = model
    self.mult = 1.0/self.model.sum()
  
  def probWord(self, ident):
    """Returns the probability of the topic emitting the given word. Only call if the model has been calculated."""
    assert((self.model!=None) and (self.mult!=None))
    return self.model[ident] * self.mult
  
  
  def getTopWords(self):
    """Returns an array of word identifiers ordered by the probability of the topic emitting them."""
    return self.model.argsort()[::-1]
