<?php
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fingerprint.proto

namespace Fingerprint;

use Google\Protobuf\Internal\GPBType;
use Google\Protobuf\Internal\RepeatedField;
use Google\Protobuf\Internal\GPBUtil;

/**
 * Generated from protobuf message <code>fingerprint.CheckDuplicateResponse</code>
 */
class CheckDuplicateResponse extends \Google\Protobuf\Internal\Message
{
    /**
     * Generated from protobuf field <code>bool isDuplicate = 1;</code>
     */
    protected $isDuplicate = false;

    /**
     * Constructor.
     *
     * @param array $data {
     *     Optional. Data for populating the Message object.
     *
     *     @type bool $isDuplicate
     * }
     */
    public function __construct($data = NULL) {
        \GPBMetadata\Fingerprint::initOnce();
        parent::__construct($data);
    }

    /**
     * Generated from protobuf field <code>bool isDuplicate = 1;</code>
     * @return bool
     */
    public function getIsDuplicate()
    {
        return $this->isDuplicate;
    }

    /**
     * Generated from protobuf field <code>bool isDuplicate = 1;</code>
     * @param bool $var
     * @return $this
     */
    public function setIsDuplicate($var)
    {
        GPBUtil::checkBool($var);
        $this->isDuplicate = $var;

        return $this;
    }

}

