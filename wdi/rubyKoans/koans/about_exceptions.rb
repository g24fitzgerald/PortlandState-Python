#11/17/17 GF notes: general flow of begin/rescue/else/ensure looks like this
# begin
#   # something which might raise an exception
# rescue SomeExceptionClass => some_variable
#   # code that deals with some exception
# rescue SomeOtherException => some_other_variable
#   # code that deals with some other exception
# else
#   # code that runs only if *no* exception was raised
# ensure
#   # ensure that this code always runs, no matter what
#   # does not change the final value of the block
# end

require File.expand_path(File.dirname(__FILE__) + '/neo')

class AboutExceptions < Neo::Koan

  class MySpecialError < RuntimeError
  end

  def test_exceptions_inherit_from_Exception
    assert_equal RuntimeError, MySpecialError.ancestors[1]
    assert_equal StandardError, MySpecialError.ancestors[2]
    assert_equal Exception, MySpecialError.ancestors[3]
    assert_equal Object, MySpecialError.ancestors[4]
  end

  #Using begin and rescue statement is error handling in Ruby, the same as
  #try/catch in other languages.
  #Different rescue statements handle different exceptions
  def test_rescue_clause
    result = nil
    begin
      fail "Oops"
    rescue StandardError => ex
      result = :exception_handled
    end

    assert_equal :exception_handled, result

    assert_equal true, ex.is_a?(StandardError), "Should be a Standard Error"
    assert_equal true, ex.is_a?(RuntimeError),  "Should be a Runtime Error"

    assert RuntimeError.ancestors.include?(StandardError),
      "RuntimeError is a subclass of StandardError"

    assert_equal "Oops", ex.message
  end

  def test_raising_a_particular_error
    result = nil
    begin
      # 'raise' and 'fail' are synonyms
      raise MySpecialError, "My Message"
    rescue MySpecialError => ex
      result = :exception_handled
    end

    assert_equal :exception_handled, result
    assert_equal "My Message", ex.message
  end

  #using begin, rescue and finally statements is error handling in Ruby
  #The same as try/catch/finally in other languages. You can have multiple
  #rescue statements to handle different exceptions.
  #An ensure statement is like a finally statemetn. It will alwasy run after all rescue statements have
  def test_ensure_clause
    result = nil
    begin
      fail "Oops"
    rescue StandardError
      # no code here
    ensure
      result = :always_run
    end

    assert_equal :always_run, result
  end

  # Sometimes, we must know about the unknown
  def test_asserting_an_error_is_raised
    # A do-end is a block, a topic to explore more later
    assert_raise(MySpecialError) do
      raise MySpecialError.new("New instances can be raised directly.")
    end
  end

end
